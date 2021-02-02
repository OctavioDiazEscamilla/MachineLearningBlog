# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 08:10:50 2021

@author: octav
"""

import praw
import pandas as pd
titulo = []
comentario = []

reddit = praw.Reddit(client_id = '-73NBm6rBipz6Q',
                     client_secret = 'g14PfYkXLE1ADACl8zNd7s98jwERJw',
                     username = 'finasensei',
                     password = 'finasensei2021',
                     user_agent ='finasensei')

wallstreetbets = reddit.subreddit('wallstreetbets')

hot1 = wallstreetbets.hot(limit=52)

#for i in hot1:
#    if not i .stickied:
#        print(i.title)
        
for submission in hot1:
    if not submission.stickied:
        print(submission.selftext)
        #titulo.append(submission.title)
        comentario.append(submission.selftext)

comentarioDF = pd.DataFrame({#'titulo': titulo, 
                             'comentario': comentario})

string = comentarioDF.to_string()

import os
currdir = os.path.dirname(__file__)
from wordcloud import WordCloud, STOPWORDS
stopwords = set(STOPWORDS)
wc = WordCloud(background_color="white", max_words=100, stopwords = stopwords)
wc.generate(string)
wc.to_file(os.path.join(currdir, "wc.png"))
    



