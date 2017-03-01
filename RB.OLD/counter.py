import csv
import sys
import re
from collections import Counter, OrderedDict
import random
import pandas

reload(sys)
sys.setdefaultencoding('utf-8')

reddit_words = dict()
chan_words = dict()
reddit_subs = ['spacedicks','askreddit','aww','books','fitness','food','funny','gaming','history','music','photography','science','technology', '4chan', 'wtf', 'todayilearned', 'news', 'jokes', 'explainlikeimfive']
chan_boards = ['<Board /b/>','<Board /c/>','<Board /ck/>','<Board /fit/>','<Board /g/>','<Board /his/>','<Board /mu/>','<Board /p/>','<Board /sci/>','<Board /v/>', '<Board /x/>', '<Board /vg/>', '<Board /vr/>', '<Board /sp/>', '<Board /diy/>', '<Board /adv/>']


def randomizer(num, length):
    list_random = list()
    while len(list_random) < num:
        rand = random.randrange(length)
        if rand not in list_random:
            list_random.append(rand)
    return list_random

def get_row(filename, sublist):
    with open(filename, 'r+') as fh:
        datareader = csv.reader(fh)
        for row in datareader:
            if row[3] in sublist:
                yield row
    return

def get_words(string):
    text = string.lower()
    words_list = re.findall(r"[\w'-]+", text)
    return words_list

'''    
for row in get_row('corpus.csv', reddit_subs):
    wordlist = get_words(row[-1])
    for word in wordlist:
        if word in reddit_words.keys():
            reddit_words[word] += 1
            if reddit_words[word] % 10000 == 0:
                print word
                print reddit_words[word]
        elif word not in reddit_words.keys():
            reddit_words[word] = 1
    
common_words_reddit = OrderedDict(Counter(reddit_words).most_common())

for key in common_words_reddit:
    value = str(common_words_reddit[key])
    common_words_reddit[key] = value

    
with open('reddit_counts_3_21.txt', 'a+') as wc:
    wc.write('    Reddit Wordcount    \n\n')
    linecounter = 1
    for key in common_words_reddit.keys():
        wc.write(str(linecounter))
        wc.write('. ')
        linecounter +=1
        wc.write(key)
        wc.write(': ')
        wc.write(common_words_reddit[key])
        wc.write('\n')
 '''        
    
for row in get_row('corpus.csv', chan_boards):
    wordlist = get_words(row[-1])
    for word in wordlist:
        chan_words[word] += 1          
        
common_words_chan = OrderedDict(Counter(chan_words).most_common())

for key in common_words_chan:
    value = str(common_words_chan[key])
    common_words_chan[key] = value

with open('4chan_counts_3_21.txt', 'a+') as wc:
    wc.write('    4chan Wordcount   \n\n')
    linecounter = 1
    for key in common_words_chan.keys():
        wc.write(str(linecounter))
        wc.write('. ')
        linecounter+=1
        wc.write(key)
        wc.write(': ')
        wc.write(common_words_chan[key])
        wc.write('\n')
