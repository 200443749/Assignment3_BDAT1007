from textblob import TextBlob
import requests
import os
import pandas as pd
import csv
import nltk
import re
import string
from nltk.sentiment import SentimentAnalyzer
from nltk.stem.porter import PorterStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.sentiment.util import *
from pymongo import MongoClient
pos_count = 0
pos_correct = 0
neg_correct = 0
neg_count = 0
positive_count=0
negative_count=0
netural_count=0
positive_list=[]
negative_list=[]
neutral_list=[]
polarity_list=[]
subjectivity_list=[]
word_list=[]
df = pd.read_csv ('analysis.csv')
test = pd.DataFrame(df)
news_data=test["Words"].dropna()
sentim_analyzer = SentimentAnalyzer()
for data in news_data:
    data=str(data)
    # remove extra white spaces
    new_data=re.sub("s+"," ", data)
    # print("WHite Space:",new_data)

    #remove punctuations
    re_pun_data=re.sub("[^-9A-Za-z ]", "" , data)
    # print("Punctuations:",re_pun_data)

    #case normalization
    text_clean = "".join([i.lower() for i in re_pun_data if i not in string.punctuation])
    # print("Normalization",text_clean)

    #Tokenizai=tion
    token_data=nltk.tokenize.word_tokenize(text_clean)
    # print("Tokenization",token_data)
    # print(token_data)
    #Stemming
    ss = nltk.SnowballStemmer(language = 'english')
    w = [ss.stem(word) for word in token_data]

    # Lemmatization
    wn = nltk.WordNetLemmatizer()
    lem_data = [wn.lemmatize(word) for word in token_data]
    for dt in lem_data:
        analysis = TextBlob(str(dt))
        if analysis.sentiment.polarity >=0:
            if analysis.sentiment.polarity > 0:
                positive_count = 1
                positive_list.append(positive_count)
            elif analysis.sentiment.polarity < 0:
                negative_count = 1
                negative_list.append(negative_count)
            else:
                netural_count = 1
                neutral_list.append(netural_count)
            word_list.append(dt)
            polarity_data=analysis.sentiment.polarity
            subjectivity_data=analysis.sentiment.subjectivity
            polarity_list.append(str(polarity_data))
            subjectivity_list.append(str(subjectivity_data))
            if analysis.sentiment.polarity > 0:
                pos_correct += 1
            pos_count +=1
            if analysis.sentiment.polarity < 0:
                neg_correct += 1
            neg_count +=1
print("Positive accuracy = {}% via {} samples".format(pos_correct/pos_count*100.0, pos_count))
print("Negative accuracy = {}% via {} samples".format(neg_correct/neg_count*100.0, neg_count))
polarity_dict={'Words':word_list,'Polarity':polarity_list,'Subjectivity':subjectivity_list,'Positive':positive_list,'Negative':negative_list,'Neutral':neutral_list}
df=pd.DataFrame.from_dict(polarity_dict,orient='index')
df.to_csv('cbc_analysis.csv')