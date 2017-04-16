# CommentBotPH

Ang mga opinyon ng isang bot, mula sa comment sections ng bias na media. 

## What?

In more technical terms, it's a Twitter bot that generates (usually) nonsensical tweets based on comments from the following Facebook pages:

* GMA News
* ABS-CBN News
* Rappler
* InterAksyon

The bot uses a Markov chain to generate tweets.

## Setup

This project requires the following modules:
* `markovify`
* `facebook-sdk` >= 3.0.0
* `tweepy`
* `requests`

The main program is in `combot.py`. It's missing a few variables that should be defined in a `key.py` file, detailed below:
* `FB_SDK_VERSION` - Facebook SDK version to use. v2.7 recommended.
* `FB_APP_xxx` - Your Facebook app's `ID` and `SECRET`.
* `TW_CONSUMER_xxx` - Consumer `KEY` and `SECRET` from Twitter.
* `TW_ACCESS_TOKEN_xxx` - Access token key and `SECRET` from Twitter.

Consult Twitter's and Facebook's docs for more info.

Modify the `pages` variable in `combot.py` to add/remove pages that will be checked.