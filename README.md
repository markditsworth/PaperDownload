# PaperDownload
Auto-downloader of ArXiv papers from Twitter

#### Requirements
Tweepy >3.5.0, requests >2.21.0, should work for any python > 2.7

### Description
If you're a nerd like me and your twitter feed regularly contains links to papers on ArXiv that you'd like to read later, but don't want to download to your phone, this is for you. I used to favorite such tweets and then later, log on to twitter on my computer and download the PDFs then. But that's pretty tendious in this day and age. Instead, now I can just reply to the tweets with "@PaperDownload" and the papers will be automatically downloaded and accessible from my device of choice.

This code works on links to ArXiv abstracts (arxiv.org/abs/...)  or any link ending in .pdf

### How to Use

Here's how you can set it up for yourselef.

1. Make a twitter account for your bot, and register it as an app. [This article](https://scotch.io/tutorials/build-a-tweet-bot-with-python) was my primary reference for this step. Once your app is registered, access and generate your API keys and Access Tokens.

2. Clone the repo in your desired location. Make sure you have all dependencies satisfied.

3. Edit `secret.py` to give your API keys and Access Tokens. They must be string type.

4. Also in `secret.py`, set `bot_handle` to your bot's handle (e.g. @give_me_knowledge) and set `username` to your username (no @).

5. Once you run `bot.py`, any arxiv paper linked in a tweet you reply to mentioning your bot will be downloaded into the working directory.

For best performance, run this bot on a small EC2 instance (or a similar cloud resource) via `screen`. The app will periodically disconnect from Twitter, but will auto-reconnect. As long as you aren't unlucky enough to envoke your bot at the same time the app is reauthenticating with the Twitter API, you will never miss a paper! Install an SFTP server on the machine to access your content from your prefered tablet or computer.
