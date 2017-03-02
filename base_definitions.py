import praw
import configparser
import time
import sys

# Functions necessary for the ini import and data checking
def data_check():
    global DATA_DIR
    if DATA_DIR == '':
        DATA_DIR = input('Please enter the directory (in the format: C:\Windows\Data\ or /Users/ExampleUser/Documents/Data/) to be used for the data storage: )
    else:
        print('Using ' + DATA_DIR + ' as directory to store data. If this is incorrect, please adjust resbot.ini')
    CONTINUE()

def master_update_check():
    global LAST_UPDATED
    global UPDATE_MASTER
    if LAST_UPDATED != DATE:
        UPDATE_MASTER = True
    print("Master Corpus is out of date, update scheduled at the end of this session.")
    else:
        UPDATE_MASTER = False
        print("Master Corpus recently updated.")

def LOGIN():
    global USERAGENT, CLIENTID, CLIENTSECRET
    if USERAGENT == '':
        USERAGENT = input('Please type in your User Agent: ')
    if CLIENTID == '':
        CLIENTID = input('Please enter your Client ID: ')
    if CLIENTSECRET == '':
        CLIENTSECRET = input('Please enter your Client Secret: ')
    PRI = praw.Reddit(user_agent = USERAGENT, client_id = CLIENTID,
                      client_secret = CLIENTSECRET)
    return PRI

def user_check():
    global USERAGENT, CLIENTID, CLIENTSECRET
    if USERAGENT in CONFIG['PRAW'] and CLIENTID in CONFIG['PRAW'] and CLIENTSECRET in CONFIG['PRAW']:
        USERAGENT = CONFIG['PRAW']['USERAGENT']
        CLIENTID = CONFIG['PRAW']['CLIENTID']
        CLIENTSECRET = CONFIG['PRAW']['CLIENTSECRET']
    else:
        print('You may add your User Agent, Client ID, and Client Secret in the resbot.ini file under PRAW if you wish to make logins easier. NOTE: THIS IS VERY UNSECURE')

def nsfw_verify():
    global NSFW_FORUMS
    print('The NSFW forums are list as: ')
    for x in NSFW_FORUMS:
        print(x)
    print('IF YOU DO NOT SEE A KNOWN NSFW FORUM, PLEASE EXIT NOW AND UPDATE RESBOT.INI')
    CONTINUE()

def CONTINUE():
    cont_quest = input("Continue? y/N    ")
    if cont_quest in {'y', 'Y', 'yes', 'Yes'}:
        return
    elif cont_quest in {'n','N','no','No'}:
        sys.exit('Exiting...')
    else:
        sys.exit("Invalid selection. Exiting for safety's sake")

def corpus_collector():
    global CORPUS_LIST, MASTER_CORPUS
    CORPUS_LIST = list(CONFIG['CORPORA'].values())
    MASTER_CORPUS = CONFIG['CORPORA']['MASTER_CORPUS']
    if MASTER_CORPUS == '':
        MASTER_CORPUS = DATA_DIR + 'master_corpus.csv'
        CONFIG.set('CORPORA', 'MASTER_CORPUS', MASTER_CORPUS)

def correlation_manager():
    global CORRELATING_FORUMS
    CORRELATING_FORUMS = {}

    for x in CONFIG.options('CORRELATIONS'):
        append_list = []
        for y in CONFIG['CORRELATIONS'][x].split(','):
            append_list.append(y)
        CORRELATING_FORUMS[x] = append_list


# This imports data from the ini file, and is arranged exactly as the base ini

CONFIG = configparser.ConfigParser()
CONFIG.read_file(open('resbot.ini'))

# IMPORTANT

print("Importing important data...")
DATA_DIR = CONFIG['IMPORTANT']['DATA_DIR']
LAST_UPDATED = CONFIG['IMPORTANT']['LAST_UPDATED']
DATE = time.strftime("%d/%m/%Y")
UPDATE_MASTER = False

data_check()
master_update_check()

# PRAW

print("Importing data for PRAW...")
USERAGENT = ''
CLIENTID = ''
CLIENTSECRET = ''

user_check()

print("Importing selections of forums...")

# REDDIT

REDDIT_SUBS = list(CONFIG['REDDIT'].values().split(','))
SFW_REDDIT_SUBS = CONFIG['REDDIT']['SFW'].split(',')
NSFW_REDDIT_SUBS = CONFIG['REDDIT']['NSFW'].split(',')

# 4CHAN

CHAN_BOARDS = list(CONFIG['4CHAN'].values().split(','))
SFW_4CHAN_BOARDS = CONFIG['4CHAN']['SFW'].split(',')
NSFW_4CHAN_BOARDS = CONFIG['4CHAN']['NSFW'].split(',')

# ALL

ALL_FORUMS = REDDIT_SUBS + CHAN_BOARDS
SFW_FORUMS = SFW_4CHAN_BOARDS + SFW_REDDIT_SUBS
NSFW_FORUMS = NSFW_REDDIT_SUBS + NSFW_4CHAN_BOARDS

# A dict of corresponding boards/subreddits with similar topics    |
# key = topic, value = list of boards/subs                        \/

correlation_manager()
UNRELATABLE_FORUMS = [x for x in ALL_FORUMS if x not in CORRELATING_FORUMS]

# REDDIT // Split down here, as this needs CORRELATING_FORUMS defined

CORR_REDDIT_SUBS = [x for x in CORRELATING_FORUMS if x in REDDIT_SUBS]
UNREL_REDDIT_SUBS = [x for x in UNRELATABLE_FORUMS if x in REDDIT_SUBS]

# 4CHAN // same

CORR_CHAN_BOARDS = [x for x in CORRELATING_FORUMS if x in CHAN_BOARDS]
UNREL_CHAN_BOARDS = [x for x in UNRELATABLE_FORUMS if x in CHAN_BOARDS]



nsfw_verify()

print("IMPORTANT: If you wish to add new subs, you will need to run forum_addition.py or modify the resbot.ini file.")

# Corpora
print('Collecting list of Corpora...')
corpus_collector()
