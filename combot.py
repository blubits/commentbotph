# -*- coding: utf-8 -*-
"""
Generates tweets from Facebook page comment sections.

:Author:     Maded Batara III
:Version:    v2.0 (2017-04-16)
"""
import facebook
import markovify
import random
import requests
import tweepy

from datetime import datetime
from keys import *

# Pages to be checked
pages = [
    ## NEWS ##
    "116724526976",     # GMA News
    "27254475167",      # ABS-CBN News
    "310621318958658",  # Rappler
    "142802334452",     # Inquirer.net
    "232388115712",     # philstar.com
    "319779186521"      # MOCHA USON BLOG
]

FB_ACCESS_TOKEN = requests.get(
    "https://graph.facebook.com/oauth/access_token?client_id={1}"
    "&client_secret={2}&grant_type=client_credentials".format(FB_SDK_VERSION, 
    FB_APP_ID, FB_APP_SECRET)
).json()["access_token"]
graph = facebook.GraphAPI(access_token=FB_ACCESS_TOKEN, version=FB_SDK_VERSION)

# Step 1. Retrieve comments from a random post
comments = []
posts = []
page = random.choice(pages)
for post in graph.get_connections(page, "posts")["data"]:
    # More than 50 comments
    popular = graph.get_connections(
        post["id"], "comments?summary=true"
    )["summary"]["total_count"] >= 50
    # Posted within today
    today = datetime.strptime(
        post["created_time"], "%Y-%m-%dT%H:%M:%S%z"
    ).date() == datetime.today().date()
    if today and popular:
        posts.append(post["id"])
post = random.choice(posts)
for comment in graph.get_all_connections(post, "comments"):
    comments.append(comment["message"])
random.shuffle(comments)

# Step 2. Generate comment
model = markovify.NewlineText('\n'.join(comments))

# Step 3. Tweet!
#auth = tweepy.OAuthHandler(TW_CONSUMER_KEY, TW_CONSUMER_SECRET)
#auth.set_access_token(TW_ACCESS_TOKEN, TW_ACCESS_TOKEN_SECRET)
#api = tweepy.API(auth)
#api.update_status(model.make_short_sentence(140))
print(model.make_short_sentence(140))