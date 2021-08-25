# importing the libraries
from bs4 import BeautifulSoup
import requests
from nltk.stem import WordNetLemmatizer
from nltk.stem import LancasterStemmer
from autocorrect import Speller
from nltk.corpus import stopwords
from langdetect import detect
import nltk, re, pprint
from nltk import word_tokenize
import spelling


def Craw_data():
   url="https://e.vnexpress.net/news/travel/stranded-in-vietnam-foreign-tourists-find-silver-lining-4339108.html"

# Make a GET request to fetch the raw HTML content
   html_content = requests.get(url).text

# Parse the html content
   soup = BeautifulSoup(html_content, 'html.parser')
# print(soup.prettify()) # print the parsed data of html
   raw=""
   for link in soup.find_all("p"):
    # print("Inner Text: {}".format(link.text))
    # print("Title: {}".format(link.get("title")))
    # print("href: {}".format(link.get("href")))
    # print(link.text)
      raw= raw + link.text
   # print("Dữ liệu thu thập đươc đã lọa bỏ tag: " +raw)

   return raw
def lanlanguge_detection():
    raw = Craw_data()
    languge_detection = detect(raw)
    print("Ngôn ngữ sử dụng: " + languge_detection)
def tokenzie():
    raw = Craw_data()
    tokens = word_tokenize(raw)
    # print("Tách các từ và hiển thị")
    # print(tokens)
    return tokens
def frequency():
   tokens= tokenzie()
   raw = Craw_data()
   frequency = tokens.count("more")
   lenth = len(raw)
   print("Số lần xuất hiện của từ More:" , int(frequency) )

   print("Tổng số chữ: " , int(lenth))

def lowercasting():
   raw = Craw_data()
   lowercasting = raw.lower()
   print("Chuyển về kiểu chữ thường: "+ lowercasting)
def stop_words():
   tokens= tokenzie()
   stop_words = set(stopwords.words('english'))
   filtered_sentence = []
   for w in tokens:
     if w not in stop_words:
         filtered_sentence.append(w)
   print("Thực hiện stop-word: "+ str(filtered_sentence))
def remove_punctuation():
   raw = Craw_data()
   tokenizer = nltk.RegexpTokenizer(r"\w+")
   new_tokens = tokenizer.tokenize(raw)
   print("Loại bỏ dấu câu: "+ str(new_tokens))
#
#
#
def Stemming_Lemmatization():
    tokens = tokenzie()
    lancaster = LancasterStemmer()
# print("{0:20}{1:20}".format("Word","lancaster Stemmer"))
# for word in tokens:
#     print("{0:20}{1:20}".format(word, lancaster.stem(word)))
#
    print("Thực hiện Stemming + Lemmatization")
    wordnet_lemmatizer = WordNetLemmatizer()
    print("{0:20}{1:20}{2:20}".format("Word","Stem","Lemma"))
    for word in tokens:
     print ("{0:20}{1:20}{2:20}".format(word,lancaster.stem(word),wordnet_lemmatizer.lemmatize(word, pos="v")))
def Save():
    raw = Craw_data()
    with open('crawl_data.txt', 'w') as file:
     file.write(raw)
     file.close()
def newline():
    document = open('crawl_data.txt')
    line =''
    for line in document:
      line +=line
    print(line.split('.'))
if __name__ == "__main__":
    Craw_data()
    lanlanguge_detection()
    tokenzie()
    frequency()
    lowercasting()
    stop_words()
    remove_punctuation()
    Stemming_Lemmatization()
    Save()
    newline()