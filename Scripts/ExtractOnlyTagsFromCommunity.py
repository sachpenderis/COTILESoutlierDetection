import os
try:
    os.mkdir("../Results Stats 1510/CommunitiesLabels/")
    for i in range(120):
        with open ("../Draft Results COTILES/Communities/strong-communities-%s.txt"%( i), 'r') as readfile:
            with open("../Draft Results COTILES/CommunitiesLabels/strong-communities-%s.txt"%(i), 'w') as writefile:
                for line in readfile:
                    #writefile.write(line.split()[0])
                    #writefile.write("\t{")
                    writefile.write(line.split("'{")[1])


except:
    pass
