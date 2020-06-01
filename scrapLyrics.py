import httplib2
from bs4 import BeautifulSoup, SoupStrainer
import re
import xlsxwriter

http = httplib2.Http()

def scrapWebPage(webPage, regex):
    list = []
    regexCompile = re.compile(regex)
    status, response = http.request(webPage)
    for link in BeautifulSoup(response, parse_only=SoupStrainer('a'), features="html.parser"):
        if link.has_attr('href'):
            if regexCompile.match(link['href']):
                list.append(link['href'])
    return list

class tamilSongs:
  def __init__(self, sno,movieName, songName, songLyrics):
    self.sno = sno
    self.movieName = movieName
    self.songName = songName
    self.songLyrics = songLyrics

moviesLink = 'https://www.tamilpaa.com/tamil-movies-list'
movieRegex = 'https:\/\/www.tamilpaa.com\/(.*)-songs-lyrics'
songRegex = 'https:\/\/www.tamilpaa.com\/[0-9]{1,3}(.*)-tamil-songs-lyrics'

moviesList = scrapWebPage(moviesLink, movieRegex)
songsList = []
i = 0
for movies in moviesList:
    songs = scrapWebPage(movies, songRegex)
    for song in songs:
        songsList.append(song)
    i += 1

i = 1
songsList = list(set(songsList))
songLyricsList = []
header = ["Sno", "Movie Name", "Song Name", "Lyrics"]
ts = tamilSongs(header[0],header[1],header[2],header[3])
songLyricsList.append(ts)
for song in songsList:
    st, rs = http.request(song)
    soup = BeautifulSoup(rs,features="html.parser")
    lyricsAll = soup.find_all('div', class_='info-box white-bg')
    if len(lyricsAll) > 0:
        lyrics = lyricsAll[0].get_text().strip()
        songName = soup.find_all('h3')[0].text.strip()
        movieName = soup.find('table', {"class": "standard mb-10px"}).find_all('tr')[0].find_all('td')[0].text
        ts = tamilSongs(i,movieName, songName, lyrics)
        songLyricsList.append(ts)
        print(i)
        i += 1


workbook = xlsxwriter.Workbook('tamilSongsLyrics.xlsx')
worksheet = workbook.add_worksheet()

row = 0
column = 0

# iterating through content list
for item in songLyricsList:
    # write operation perform
    worksheet.write(row, column, item.sno)
    worksheet.write(row, column + 1, "\""+item.songName +"\"")
    worksheet.write(row, column + 2, "\""+item.movieName+"\"")
    worksheet.write(row, column + 3, "\""+item.songLyrics.replace('\"', '')+"\"")

    # incrementing the value of row by one
    # with each iteratons.
    row += 1

workbook.close()

