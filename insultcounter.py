import csv


def perReader(insultfile, outname, total, percent):
    fifctr = 0
    with open(insultfile, 'r') as insf:
        reader = csv.reader(insf)
        for row in reader:
            if float(row[0]) > percent:
                fifctr +=1
    outString = outname + ' above ' + str(percent*100) +' at '+ str(fifctr) + ' of ' + str(total)
    return outString
    
   
def run(outfile, runList):
    with open(outfile, 'a+') as out:
        out.write('Above 50%\n\n')
    for x in runList:
        nextLine = perReader(x[0],x[1],x[2],0.50)
        with open(outfile, 'a+') as of:
            of.write(nextLine)
            of.write('\n')
    with open(outfile, 'a+') as out:
        out.write('\n\nAbove 75%\n\n')
    for x in runList:
        nextLine = perReader(x[0],x[1],x[2],0.75)
        with open(outfile, 'a+') as of:
            of.write(nextLine)
            of.write('\n')
    with open(outfile, 'a+') as out:
        out.write('\n\nAbove 90%\n\n')
    for x in runList:
        nextLine = perReader(x[0],x[1],x[2],0.90)
        with open(outfile, 'a+') as of:
            of.write(nextLine)
            of.write('\n')
      
insultfileList = [['reddit_insult_preds.csv','Reddit',428888],['4chan_insult_preds.csv','4Chan',1037700],['r4chan_insult_preds.csv','r4Chan',22760],
['noshock_insult_preds.csv','Reddit w/out Shock Sites', 349068],['shock_insult_preds.csv', 'Reddit Shocksites',57060],
['nob_insult_preds.csv', '4Chan without /b/', 991424],['only_b_insult_preds.csv', '/b/',46276]]

if __name__=="__main__":
    run('Insult_Predictions.txt',insultfileList)
