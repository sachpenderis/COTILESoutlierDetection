import os


month= 60*60*24*30
ttl = 30
firstTimestamp = 1278777417
try:
    os.mkdir("../ResultsEtiles%s30/Graph1/" % ttl)
except:
    pass

with open ("../Datasets/NetworkStats.txt", 'r') as readfile:
    i=0
    for line in readfile:
        with open("../ResultsEtiles%s30/Graph1/graph%s.txt" % (ttl,i), 'a') as writefile:

            if (int(line.split()[2]) < (firstTimestamp + month)):
                writefile.write("%s\t%s\t%s\t%s\n"%(int(line.split()[0]), int(line.split()[1]), line.split()[2], line.split()[3]))
            else:
                i+=1
                firstTimestamp+=month



