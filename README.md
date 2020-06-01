# Tamil-lyrics-generator-NLP
Web scrapping and NLP project for generating lyrics from web scrapped lyrics Dataset. 

# Generating lyrics in Tamil using Deep Learning with TensorFlow and Webscrapping with BeautifulSoap

Text generation can be done through simply predicting the next most likely word, given an input sequence. This can be done over and over by feeding the original input sequence, plus the newly predicted end word, as the next input sequence to the model. As such, the full output generated from a very short original input can effectively go on however long you want it to be.  

**TensorFlow** provides number of libraries for NLP in Deep learning. Used Deep neural network to generate the sequence of tamil words from the tamil songs lyrics dataset which has been scrapped from 
[tamilpaa.com](https://www.tamilpaa.com/).  

scrapLyrics.py file scraps the data from the website and created a .xlsx file from it.
Used **Google Colab** to implement TensorFlow neural networks in the file,    
 
Dataset is now available at https://www.kaggle.com/sivaskvs/tamil-songs-lyrics-dataset 

## Getting Started

Some of the major libraries used in this project.

* Neural networks with **TensorFlow**
* tensorflow.keras.preprocessing.text and tensorflow.keras.preprocessing.sequence for tokenizing and preprocessing the lyrics dataset
* Web Scrapping with **BeautifulSoap**
* **Numpy** and **Pandas** for interacting with Dataframes
* Creating  excel file with **xlsxwriter**
* **google.colab** for interacting with the google drive


### Sample Input and Output

Input 
```
சிவாவின் தொழில்நுட்ப காதல்
```

Output
```
சிவாவின் தொழில்நுட்ப காதல் தூங்கும் அந்தி மனம் பாடும் பாடல் பாதி உலகமே நாளை பேபி பேபி பேபி அழகே என் மனமே மனமே போகாதே என்றே கண்கள் என்றே என் கண்மணி முன்னே முன்னே முன்னே எப்போ வெளியே போகிறாய் திரும்ப மண்ணும் கொஞ்சி முன்னே வரும் அழகி தன் வீசும் அவள் வா வா நிலவே வா ஏனடி வெயில் வரும் என்று ஏத்தி பற சிங்கார சிங்கார சிங்கார ஹம்மா அடியாத்தி அடியாத்தி அடியாத்தி அடியாத்தி அடியாத்தி அடியாத்தி அடியாத்தி இதயத்தில் தானடி லலலா என்னக் ஆத்தா என்னக் எம்மா மன்மத ஓ வேணுமா ம் இன் ஏ மொத்த அந்த தானே ஹம்மா சிங்கார சிங்கார சிங்கார ராமா சிங்கார முகவரி என்னக் தோழா சிங்கார என்னக் அடியாத்தி உடனே என்னக் என்னக் அடுத்த அடுத்த அடியாத்தி பாஸ் அடியாத்தி ராமா ராமா ராமா ராமா ராமா உடனே அடியாத்தி
```

### Installing
```
pip install {Mentioned Libraries}
or
pip3 install {Mentioned Libraries}
```

## Acknowledgments

* [tamilpaa.com](www.https://www.tamilpaa.com//)
