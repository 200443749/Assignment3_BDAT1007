from flask import Flask, render_template, session, request, redirect
from flask import Flask, jsonify, render_template, url_for
from bs4 import BeautifulSoup
import requests
import os
import pandas as pd
import csv

urls=["https://www.cbc.ca/news/canada/toronto"]
name_list=[]
price_list=[]
price_match_list=[]
namee_list=[]
review_list=[]
rating=[]
revieww_list=[]
source_list=[]
post_date_list=[]
news_list=[]
for i in range(len(urls)):
    source=requests.get(urls[i])
    soup=BeautifulSoup(source.text,'html')
    title_name=soup.find_all('div',class_='card-content-top')
    source_name=soup.find_all('div',class_='metadataText')
    posted_date=soup.find_all('div',class_='metadataText')
    news=soup.find_all('div',class_='card-content-top')
    # Title Name list
    for i in title_name:
        h3=i.find('h3')
        if h3 is not None:
            name_list.append(h3.text)
            namee_list=list(map(lambda x:x.strip(),name_list))
    # Source Name list
    for i in source_name:
        source=i.find('span')
        if source is not None:
            source_list.append(source.text)
    # Time list
    for i in posted_date:
        post_date=i.find('time')
        if post_date is not None:
            post_date_list.append(post_date.text)
    # Guitar Name list
    for i in news:
        news_data=i.find('div')
        if news_data is not None:
            news_list.append(news_data.text)
print(news_list)
di1={'title': namee_list,'news':news_list,'Posted Date':post_date_list,'Source':source_list}
df = pd.DataFrame.from_dict(di1,orient='index')
df.transpose()
df.to_csv('cbc.csv')