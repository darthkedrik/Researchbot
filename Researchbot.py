import configparser
import time
import sys

DATE = time.strftime("%d/%m/%Y")

CONFIG = configparser.ConfigParser()
CONFIG.read_file(open('resbot.ini'))

# Necessary functions defined first, then the program will run
def scrape_questions(site):
    q1 = input('Would you like to scrape ' + site + '? y/N    ')
    if q1 in {'y','Y','yes','Yes'}:
        print(site + " will be scanned and scraped.")
        site_scrape = True
        q2 = input('Would you like to analyze ' + site + '? y/N    ')
        if q2 in {'y','Y','Yes','yes'}:
            print('New ' + site + ' data will be analyzed.')
            site_analysis = True
        elif q2 in {'n','N','no','No'}:
            print('Data will not be analyzed.')
            site_analysis = False
        else:
            print('Invalid selection. Will not analyze.')
            site_analysis = False
    elif q1 in {'n','N','no','No'}:
        print(site + " will not be scanned.")
        site_scrape = False
        site_analysis = False
    else:
        print('Invalid selection. By default, ' + site + ' will not be scanned.')
        site_analysis = False
    answers = [site_scrape, site_analysis]
    return answers

def forum_list_selection(site):
    print('Please select which ' + site + ' forums list to scrape (NOTE: Be sure to type your selection EXACTLY as it appears in the list)')
    chan_selections = {'ALL' : CHAN_BOARDS, 'NSFW' : NSFW_4CHAN_BOARDS, 'SFW' : SFW_4CHAN_BOARDS,
                       'CORR' : CORR_CHAN_BOARDS, 'UNREL' : UNREL_CHAN_BOARDS}
    reddit_selections = {'ALL' : REDDIT_SUBS, 'NSFW' : NSFW_REDDIT_SUBS, 'SFW' : SFW_REDDIT_SUBS,
                         'CORR' : CORR_REDDIT_SUBS, 'UNREL' : UNREL_REDDIT_SUBS}
    selection = input('ALL    NSFW    SFW    CORR    UNREL')
    if selection not in ('ALL', 'NSFW', 'SFW', 'CORR', 'UNREL'):
        selection = input('ALL    NSFW    SFW    CORR    UNREL')
    if site == 'reddit':
        return reddit_selections[selection]
    elif site == '4chan':
        return chan_selections[selection]
    else:
        # Throw an error

def primary(site, answers):
    if answers[0] == True:
        if site == 'reddit':
            sub_list = forum_list_selection(site)
            r_scraper.spybot(sub_list)
            if answers[1] == True:
                r_analysis
        elif site == '4chan':
            b_list = forum_list_selection(site)
            c_scraper.spybot(b_list)
            if answers[1] == True:
                c_analysis
        else:
            # throw an error

# Get the directory for the data
if CONFIG['IMPORTANT']['DATA_DIR'] == '':
    DATA_DIR=input('Please enter the directory (in the format: C:\Windows\Data\ or /Users/ExampleUser/Documents/Data/) to be used for the data storage: )
else:
    DATA_DIR = CONFIG['IMPORTANT']['DATA_DIR']
    print('Using ' + DATA_DIR + ' as directory to store data.')


LAST_UPDATED = CONFIG['IMPORTANT']['LAST UPDATED']
if LAST_UPDATED != DATE:
    UPDATE_MASTER = True
    print("Master Corpus is out of date, update scheduled at the end of this session.")
else:
    UPDATE_MASTER = False
    print("Master Corpus recently updated.")

print("Importing data for PRAW...")
USERAGENT = CONFIG['PRAW']['USERAGENT']
CLIENTID = CONFIG['PRAW']['CLIENT_ID']
print("PRAW data imported.")

print("Importing selections of forums...")
REDDIT_SUBS = list(CONFIG['REDDIT'].values())
SFW_REDDIT_SUBS = CONFIG['REDDIT']['SFW']
NSFW_REDDIT_SUBS = CONFIG['REDDIT']['NSFW']
CHAN_BOARDS = list(CONFIG['4CHAN'].values())
SFW_4CHAN_BOARDS = CONFIG['4CHAN']['SFW']
NSFW_4CHAN_BOARDS = CONFIG['4CHAN']['NSFW']
ALL_FORUMS = REDDIT_SUBS + CHAN_BOARDS
SFW_FORUMS = SFW_4CHAN_BOARDS + SFW_REDDIT_SUBS
NSFW_FORUMS = NSFW_REDDIT_SUBS + NSFW_4CHAN_BOARDS
CORRELATING_FORUMS = CONFIG['CORRELATIONS']
UNRELATABLE_FORUMS = [x for x in ALL_FORUMS if x not in CORRELATING_FORUMS]
CORR_REDDIT_SUBS = [x for x in CORRELATING_FORUMS if x in REDDIT_SUBS]
UNREL_REDDIT_SUBS = [x for x in UNRELATABLE_FORUMS if x in REDDIT_SUBS]
CORR_CHAN_BOARDS = [x for x in CORRELATING_FORUMS if x in CHAN_BOARDS]
UNREL_CHAN_BOARDS = [x for x in UNRELATABLE_FORUMS if x in CHAN_BOARDS]

print("Forum selections imported.")
print("NSFW Forums are listed as: ")
for x in NSFW_FORUMS:
    print(x)
print("WARNING: If you do not see a NSFW sub you've added in this list, please exit now and check the configuration file to make sure all information is correct.")

cont_quest = input("Continue? y/N    ")
if cont_quest in {'y','Y','yes','Yes'}:
    pass
elif cont_quest in {'n','N','no','No'}:
    sys.exit('Exiting...')
else:
    sys.exit("Invalid selection, breaking as default.")

print("IMPORTANT: If you wish to add new subs, you will need to run forum_addition.py or modify the resbot.ini file.")

print("Collecting list of Corpora...")
CORPUS_LIST = list(CONFIG['CORPORA'].values())
if MASTER_CORPUS == '':
    MASTER_CORPUS = DATA_DIR + 'master_corpus.csv'

print('By default this program is made for Reddit and 4chan, if you wish to scrape other sites you may use this as a template, but will need to develop a scraper for the new site and modify this file.')

reddit_answers = scrape_questions('reddit')
chan_answers = scrape_questions('4chan')

# Would be great if we could use the ALL_FORUMS instead of calling each separately,
# but that just won't work without writing a whole lot more than necessary. This
# is this simplest.
primary('reddit', reddit_answers)
primary('chan', chan_answers)




'''

Make this check resbot.cfg, importing DATA_DIR, predefined boards lists,
and existing corpus plus last run date

if the resbot.cfg file is empty, it will ask the user to populate it

It will then print out the config.md files as entered, whichever option
selected above

Then it will ask if user wishes to update any of these, and if they do it will
iterate through asking if update needed

All entered values will then be written to config.md

__main__ will now ask if user wishes to collect from 4chan, reddit, or both
and then run corresponding spybots and corpus functions

before it actually runs, it will ask if the user wishes to update the master
corpus, and if so will automatically append to the master corpus as well


Very good idea: Include twitter analysis

'''
