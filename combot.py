# -*- coding: utf-8 -*-
"""
Generates comments from

:Author:     Maded Batara III
:Version:    v1.0dev (Date)
"""
import facebook
import markovify
import random
import tweepy

from keys import *

# Pages to be checked
pages = [
    ## NEWS ##
    "116724526976",     # GMA News
    "27254475167",      # ABS-CBN News
    "192300027461534",  # InterAksyon
    "310621318958658",  # Rappler
    "142802334452",     # Inquirer.net
    "232388115712",     # philstar.com
    ## #DU30 PAGES ##
    #"782788691807807",  # "Rody Duterte Supporters OFW Global Movement"
    #"220199051378",     # Duterte Today
    #"319779186521"      # MOCHA USON BLOG
]

# Step 1. Retrieve comments from recent posts
graph = facebook.GraphAPI(access_token=ACCESS_TOKEN_FACEBOOK, version="2.5")
comments = []
for page in pages:
    for post in graph.get_connections(page, "posts")["data"]:
        for comment in graph.get_connections(post["id"], "comments")["data"]:
            comments.append(comment["message"])

random.shuffle(comments)

# Step 2. Generate comment
model = markovify.NewlineText('\n'.join(comments))

# Step 3. Tweet!
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN_TWITTER, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
api.update_status(model.make_short_sentence(140))