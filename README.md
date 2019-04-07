# PaperDownload
Auto-downloader of ArXiv papers from Twitter

#### Requirements
Tweepy >3.5.0, requests >2.21.0

### How To Use
If you're a nerd like me and your twitter feed regularly contains links to papers on ArXiv that you'd like to read later, but don't want to download to your phone, this is for you. I used to favorite such tweets and then later, log on to twitter on my computer and download the PDFs then. But that's pretty tendious in this day and age. Instead, now I can just reply to the tweets with "@PaperDownload" and the papers will be automatically downloaded on my device of choice.

Here's how you can set it up for yourselef.

1. Make a twitter account for your bot, and register it as an app. [This article](https://scotch.io/tutorials/build-a-tweet-bot-with-python) was my primary reference for this step. Once your app is registered, access and generate your API keys and Access Tokens.

2. Clone the repo in your desired location. Make sure you have all dependencies satisfied.

3. Edit `secret.py` to give your API keys and Access Tokens. They must be string type.

4. Edit line 32 of `bot.py` so that it reads 
python```
if username == '<your screen name>':``` 
so that your bot will only respond to your personal twitter handle.

5. Edit line 41 of `bot.py` so that it reads 
python```
stream.filter(track=['@<the screen name of the bot you created in step 1>'])```
so that your bot is triggered when it is mentioned in a reply.

6. Once you run the code, any arxiv paper linked in a tweet you reply to mentioning your bot will be downloaded into the working directory.

If you run the application on the device you will be reading/printing the paper from, it should always be online for the functionality to work. In my case, my device will not always be online (or on for that matter). So I have a free-tier cloud compute resource running the bot application, in conjunction with an sftp server. Whenever I invoke the bot on Twitter, the paper will be downloaded to cloud storage, and I can access it through the sftp client on my tablet.
