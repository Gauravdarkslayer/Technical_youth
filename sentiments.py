#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!python -m pip install textblob
from flask import Flask , jsonify,request,send_from_directory
import requests
from textblob import TextBlob
import os
import  tweepy
# import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from zipfile import ZipFile


# In[2]:


consumerKey = 'b07gbNXNXIrGTlkYxlZETSRWc'
consumerSecret = 'LjNXFp0lSq7Jm3xFx69XP8K1Y2jO8HawDLGcJheuZiRVkTqnKy'
accessToken = '2489780862-02zsyduWQnCwiBz1zsTXj6k4595UeRptdnVH9o5'
accessTokenSecret = 'Txm2djO7IYJ6cZn0FTVX1q9vXXr19YYvPzWym1sTiQ94u'

# In[3]:

auth = tweepy.OAuthHandler(consumer_key=consumerKey, consumer_secret=consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)



def percentage(part, whole):
    return 100* float(part)/float(whole)

# UPLOAD_FOLDER = 'E:/project'

# app=Flask(__name__)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# @app.route('/',methods=['GET','POST'])
# def index():
#     some_json=request.get_json()
#     if(request.method=='POST'):
#         return jsonify({'you':some_json}),201
#     else:
#         return jsonify({'about':'hello world !!'})
# @app.route('/percentage/<path:search>', methods=['GET', 'POST'])
def per(search):

    searchTerm =  search #input("Enter keyword/hashtag to search")
    noofSearchTerms = 50

    tweets = tweepy.Cursor(api.search, q=searchTerm).items(noofSearchTerms)


    positive = 0
    negative = 0
    neutral = 0
    polarity = 0
    neutral_data = []
    positive_data = []
    negative_data = []

    # print(type(tweets))
    for tweet in tweets:
        analysis = TextBlob(tweet.text)
        polarity += analysis.sentiment.polarity
        # print("This is analysis",analysis)
        # print("This is polarity",polarity)
        #     print(type(analysis))
        print(tweet.favorite_count)
        if (analysis.sentiment.polarity == 0):
            neutral += 1
            neutral_data.append((tweet.retweet_count,str(analysis),))
        elif (analysis.sentiment.polarity < 0.00):
            negative += 1
            negative_data.append((tweet.retweet_count,str(analysis)))
        elif (analysis.sentiment.polarity > 0.00):
            positive += 1
            positive_data.append((tweet.retweet_count,str(analysis)))
    neutral_data.sort(reverse=True)
    negative_data.sort(reverse=True)
    positive_data.sort(reverse=True)
    print("Top Neutral Tweets are ",neutral_data[:3])
    print("Top Negative Tweets are ",negative_data[:3])
    print("Top Postive Tweets are ",positive_data[:3])
    positive =percentage(positive, noofSearchTerms)
    negative =percentage(negative, noofSearchTerms)
    neutral =percentage(neutral, noofSearchTerms)
    polarity = percentage(polarity, noofSearchTerms)

    positive = format(positive, '.2f')
    negative = format(negative, '.2f')
    neutral = format(neutral, '.2f')

    neutral_data1 = pd.DataFrame(neutral_data)
    positive_data1 = pd.DataFrame(positive_data)
    negative_data1 = pd.DataFrame(negative_data)
    writer=pd.ExcelWriter("neutral_data"+".xlsx",engine="xlsxwriter")
    neutral_data1.to_excel(writer,"Sheet1")
    writer.save()

    writer=pd.ExcelWriter("positive_data"+".xlsx",engine="xlsxwriter")
    positive_data1.to_excel(writer,"Sheet1")
    writer.save()

    writer=pd.ExcelWriter("negative_data"+".xlsx",engine="xlsxwriter")
    negative_data1.to_excel(writer,"Sheet1")
    writer.save()
    with ZipFile('combined.zip', 'w') as zipObj:
       # Add multiple files to the zip
       zipObj.write('neutral_data.xlsx')
       zipObj.write('positive_data.xlsx')
       zipObj.write('negative_data.xlsx')

    os.remove("neutral_data.xlsx")
    os.remove("positive_data.xlsx")
    os.remove("negative_data.xlsx")
    sresults=str(positive)+","+str(neutral)+","+str(negative)
    # return jsonify({'result':sresults})

per("chandrayaan")

# In[ ]:



# In[ ]:

# @app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
# def download(filename):
#     uploads = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])
#  #   return send_from_directory(directory=uploads, filename=filename)

#app.run(host='localhost',debug=True,port=8000)
