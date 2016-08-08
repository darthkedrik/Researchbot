from __future__ import division
import csv


def sentiAvg(filehandle, sentiPos = 0):
    with open(filehandle, 'r+') as fh:
        r = csv.reader(fh)
        sentiCtr = 0
        sentiTot = 0.0
        for row in r:
            sentiTot += float(row[sentiPos])
            sentiCtr +=1
    senti = sentiTot / sentiCtr
    return senti
    
def sentiCommon(filehandle):
    with open(filehandle, 'r+') as fh:
        r = csv.reader(fh)
        sentiCtr = 0
        sentiNeg = 0
        sentiPos = 0
        sentiNeu = 0
        veryNeut = 0
        for row in r:
            rowNeg = float(row[0])
            rowPos = float(row[2])
            rowNeu = float(row[1])
            if rowNeg > rowPos and rowNeg > rowNeu:
                sentiNeg +=1
            elif rowPos > rowNeg and rowPos >rowNeu:
                sentiPos +=1
            elif rowNeu >= 0.75:
                veryNeut += 1
            elif rowNeu > rowNeg and rowNeu > rowPos and rowNeu <0.75:
                sentiNeu +=1
            else:
                pass
            sentiCtr += 1
    tNeg = sentiNeg / sentiCtr
    tPos = sentiPos / sentiCtr
    tNeu = sentiNeu / sentiCtr
    vtneu = veryNeut / sentiCtr
    output = {'tNeg' :  tNeg,
                'tPos' : tPos,
                'tNeu' : tNeu,
                'CompletelyNeutral' : vtneu}
    return output
    
    
redNeg = sentiAvg('reddit_sentiments.csv')
redPos = sentiAvg('reddit_sentiments.csv', sentiPos = 2)
redNeu = sentiAvg('reddit_sentiments.csv', sentiPos = 1)

print 'The average sentiments on Reddit are: Negative: ', redNeg, " Positive: ", redPos, " and Neutral: ", redNeu

chanNeg = sentiAvg('4chan_sentiments.csv')
chanPos = sentiAvg('4chan_sentiments.csv', sentiPos = 2)
chanNeu = sentiAvg('4chan_sentiments.csv', sentiPos = 1)

print 'The average sentiments on 4chan are: Negative: ', chanNeg, " Positive: ", chanNeg, " and Neutral: ", chanNeu

redTot = sentiCommon('reddit_sentiments.csv')
chanTot = sentiCommon('4chan_sentiments.csv')

print redTot
print chanTot
