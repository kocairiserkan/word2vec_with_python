import pandas as pd
import gensim
from nltk.tokenize import word_tokenize


df = pd.read_csv("file_name.csv")


words = []
for i in df["sentences"]:
    words.append(word_tokenize(i)) 
    
w2v = gensim.models.Word2Vec(words,size=150,window=10,min_count=2,workers=10,iter=10)

w1 = "hayvan"
m1 = w2v.most_similar(positive=w1, topn=5)
print("hayvan kelimesine benzer 5 kelime ve oranları:",m1 ,"/n")

w2 = "belediye" 
m2 = w2v.most_similar(positive=w2, topn=5)
print("belediye kelimesine benzer 5 kelime ve oranları:",m2 ,"/n")


w3 = "kadın" 
m3 = w2v.most_similar(positive=w3, topn=5)
print("kadın kelimesine benzer 5 kelime ve oranları:",m3 ,"/n")

w4 = "sağlık" 
m4 = w2v.most_similar(positive=w4, topn=5)
print("sağlık kelimesine benzer 5 kelime ve oranları:",m4 ,"/n")


w5 = "kitap" 
m5 = w2v.most_similar(positive=w5, topn=5)
print("kitap kelimesine benzer 5 kelime ve oranları:",m5 ,"/n")





