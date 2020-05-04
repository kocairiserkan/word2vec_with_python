from bs4 import BeautifulSoup
import requests
import re
from nltk.tokenize import word_tokenize
import pandas as pd



url = ""
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, "html.parser")
page = soup.find_all("p")


news = []
for p in page:
    news.append(p)


# cleaning
sentences = []
for h in range(len(news)):
    review = re.sub(r'\W', ' ', str(news[h]))
    review = re.sub(r'\s\w\s', ' ', review)
    review = re.sub(r'^\w\s', ' ', review)
    review = re.sub('strong',' ', review)
    review = re.sub('class',' ', review)
    review = re.sub(r'\s+', ' ', review)
    review = re.sub(r'^\s','', review)
    review=review.lower()
    sentences.append(review)


word_count= []
for c in sentences:
    word_count.append(len(word_tokenize(c)))
    
segment_no= []
for i in range(len(sentences)):
    segment_no.append(i)
    
url_no = []
for i in range(len(sentences)):
    url_no.append(url)


data=pd.DataFrame({
       "url": url_no,
       "segment_no":segment_no,
       "sentences":sentences,
       "word_count":word_count
        })

data.to_csv("file_name.csv", sep = ',', encoding = 'utf-8', index = False, mode = "a")










