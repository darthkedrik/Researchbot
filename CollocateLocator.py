import csv
import nltk
import re
import sys
from nltk.collocations import *
bigram_measures = nltk.collocations.BigramAssocMeasures()

reload(sys)
sys.setdefaultencoding('utf-8')

def csvReader(filename, sublist):
    comments = []
    with open(filename, 'r') as fn:
        reader = csv.reader(fn)
        for row in reader:
            if row[3] in sublist:
                comments.append(row[-1])
    return comments
    
def words(comment):
    text = comment.lower()
    words = re.findall(r"[\w'-]+", text)
    return words
    
def textLump(commList):
    strLump = ''
    for comment in commList:
        strLump = strLump + comment + ' '
    return strLump
    
def run(word, corpus, sublist):
    wordFilter = lambda *w: word not in w
    comments_list = csvReader(corpus, sublist)
    selectString = textLump(comments_list)
    wordList = words(selectString)
    finder = BigramCollocationFinder.from_words(wordList)
    finder.apply_ngram_filter(wordFilter)
    with open("naughty_word_collocates.txt", 'a+') as nwc:
        for sub in sublist:
            nwc.write(sub)
            nwc.write(', ')
        nwc.write('\n\n\n')
        for n in finder.nbest(bigram_measures.pmi, 20):
            nwc.write(str(n))
            nwc.write('\n')                            
        
badwords = ['fuck', 'shit', 'damn', 'ass', 'bitch', 'faggot', 'fucking', 'fag', 'asshole', 'cunt']
reddit_subs = ['spacedicks','askreddit','aww','books','fitness','food','funny','gaming','history','music','photography','science','technology', '4chan', 'wtf', 'todayilearned', 'news', 'jokes', 'explainlikeimfive']
chan_boards = ['<Board /b/>','<Board /c/>','<Board /ck/>','<Board /fit/>','<Board /g/>','<Board /his/>','<Board /mu/>','<Board /p/>','<Board /sci/>','<Board /v/>', '<Board /x/>', '<Board /vg/>', '<Board /vr/>', '<Board /sp/>', '<Board /diy/>', '<Board /adv/>']
reddit_shock_subs = ['spacedicks', 'wtf']
reddit_chan = ['4chan']
reddit_no_shock = ['askreddit','aww','books','fitness','food','funny','gaming','history','music','photography','science','technology', 'todayilearned', 'news', 'jokes', 'explainlikeimfive']
chan_no_b = ['<Board /c/>','<Board /ck/>','<Board /fit/>','<Board /g/>','<Board /his/>','<Board /mu/>','<Board /p/>','<Board /sci/>','<Board /v/>', '<Board /x/>', '<Board /vg/>', '<Board /vr/>', '<Board /sp/>', '<Board /diy/>', '<Board /adv/>']
chan_only_b = ['<Board /b/>']

list_of_lists =[reddit_subs, chan_boards, reddit_shock_subs, reddit_chan, reddit_no_shock, chan_no_b, chan_only_b]

for l in list_of_lists:
    for w in badwords:
        run(w, 'corpus.csv', l)