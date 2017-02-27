import praw

# Check if the Master Corpus is out of date
global UPDATE_MASTER
global LAST_UPDATED
global DATE

global DATA_DIR

global USERAGENT
global CLIENTID
global CLIENTSECRET

def LOGIN():
    if USERAGENT == None:
        USERAGENT = input('Please type in your User Agent: ')
    if CLIENTID == None:
        CLIENTID = input('Please enter your Client ID: ')
    if CLIENTSECRET == None:
        CLIENTSECRET = input('Please enter your Client Secret: ')
    PRI = praw.Reddit(user_agent = USERAGENT, client_id = CLIENTID,
                      client_secret = CLIENTSECRET)
    return PRI


# Pre-defined subreddit and board groups
global REDDIT_SUBS
global SFW_REDDIT_SUBS
global NSFW_REDDIT_SUBS
global UNRELATABLE_FORUMS
global SFW_4CHAN_BOARDS
global CHAN_BOARDS
global NSFW_4CHAN_BOARDS
global ALL_FORUMS
global NSFW_FORUMS
global SFW_FORUMS
global CORR_REDDIT_SUBS
global UNREL_REDDIT_SUBS
global CORR_CHAN_BOARDS
global UNREL_CHAN_BOARDS

# A dict of corresponding boards/subreddits with similar topics
# key = topic, value = list of boards/subs
global CORRELATING_FORUMS

# Corpus file names, as well as most recent update to master corpus
global CORPUS_LIST
global MASTER_CORPUS
