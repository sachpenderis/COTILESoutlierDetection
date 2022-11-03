import os

try:
    os.mkdir("../Results Stats 1510/CommunitiesOnlyMembers/")
    for i in range(120):
        with open ("../Draft Results COTILES/Communities/strong-communities-%s.txt"%(i), 'r') as readfile:
            with open("../Draft Results COTILES/CommunitiesOnlyMembers/strong-communities-%s.txt"%(i), 'a') as writefile:
                for line in readfile:
                        writefile.write("%s\n"%line.split('[')[1].split(']')[0])


except:
    pass