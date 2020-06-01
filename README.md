# Tamil-lyrics-generator-NLP
Web scrapping and NLP project for generating lyrics from web scrapped lyrics Dataset. 

# Generating lyrics in Tamil using Deep Learning with TensorFlow and Webscrapping with BeautifulSoap

Text generation can be done through simply predicting the next most likely word, given an input sequence. This can be done over and over by feeding the original input sequence, plus the newly predicted end word, as the next input sequence to the model. As such, the full output generated from a very short original input can effectively go on however long you want it to be.  

**TensorFlow** provides number of libraries for NLP in Deep learning. Used Deep neural network to generate the sequence of tamil words from the tamil songs lyrics dataset which has been scrapped from 
[tamilpaa.com](https://www.tamilpaa.com/).  

retrieveLyrics.py file scraps the data from the website and created a .xlsx file from it.
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

```

### Installing
```
pip install {Mentioned Libraries}
or
pip3 install {Mentioned Libraries}
```

## Acknowledgments

* [tamilpaa.com](www.https://www.tamilpaa.com//)
