

with open('reddit_total_counts_3_23.txt', 'r') as fh:
    ctr = 0
    totperc = 0

    for line in fh.readline():
        print line
        linelist = line.split()
        integer = float(linelist[0])
        

        if integer in range(44,266):
            lineperc = float(float(linelist[-1])/49942433)
            ctr += 1
            totperc += lineperc
        else:
            continue
    standev = totperc/ctr
    
print standev