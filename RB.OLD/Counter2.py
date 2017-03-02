from collections import Counter
import re
import csv
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

if len(sys.argv) < 2:
    print "Please input appropriate .csv file."
    sys.exit()

chanctr = Counter()
redditctr = Counter()

reddit_subs = ['spacedicks','askreddit','aww','books','fitness','food','funny','gaming','history','music','photography','science','technology', '4chan', 'wtf', 'todayilearned', 'news', 'jokes', 'explainlikeimfive']
chan_boards = ['<Board /b/>','<Board /c/>','<Board /ck/>','<Board /fit/>','<Board /g/>','<Board /his/>','<Board /mu/>','<Board /p/>','<Board /sci/>','<Board /v/>', '<Board /x/>', '<Board /vg/>', '<Board /vr/>', '<Board /sp/>', '<Board /diy/>', '<Board /adv/>']
reddit_shock_subs = ['spacedicks', 'wtf']
reddit_chan = ['4chan']
reddit_no_shock = ['askreddit','aww','books','fitness','food','funny','gaming','history','music','photography','science','technology', 'todayilearned', 'news', 'jokes', 'explainlikeimfive']
chan_no_b = ['<Board /c/>','<Board /ck/>','<Board /fit/>','<Board /g/>','<Board /his/>','<Board /mu/>','<Board /p/>','<Board /sci/>','<Board /v/>', '<Board /x/>', '<Board /vg/>', '<Board /vr/>', '<Board /sp/>', '<Board /diy/>', '<Board /adv/>']
chan_only_b = ['<Board /b/>']

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
    
for row in get_row('corpus.csv', chan_boards):
    wordlist = get_words(row[-1])
    for word in wordlist:
        chanctr[word] +=1

with open('4chan_counts_3_.txt', 'a+') as wc:
    wc.write('    /b/ Wordcount   \n\n')
    linecounter = 1
    total_chan_count = sum(chanctr.values())
    wc.write('Total Word Count: ')
    wc.write(str(total_chan_count))
    wc.write('\n\n')
    for word, count in chanctr.most_common():
        wc.write(str(linecounter))
        linecounter +=1
        wc.write('. ')
        wc.write(word)
        wc.write(' ')
        wc.write(str(count))
        wc.write('\n')
        
        
        
for row in get_row('corpus.csv', reddit_subs):
    wordlist = get_words(row[-1])
    for word in wordlist:
        redditctr[word] +=1

with open('reddit_counts_3_.txt', 'a+') as wc:
    wc.write('    Reddit Wordcount   \n\n')
    linecounter = 1
    total_reddit_count = sum(redditctr.values())
    wc.write('Total Word Count: ')
    wc.write(str(total_reddit_count))
    wc.write('\n\n')
    for word, count in redditctr.most_common():
        wc.write(str(linecounter))
        linecounter +=1
        wc.write('. ')
        wc.write(word)
        wc.write(' ')
        wc.write(str(count))
        wc.write('\n')
