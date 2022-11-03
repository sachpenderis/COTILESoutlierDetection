

with open("../Draft Results COTILES/Chain.txt", 'a') as writefile:
    with open("../Draft Results COTILES/Merged.txt", 'r') as readfile:
        for line in readfile:
            node = line.split()[0]
            writefile.write("\n%s\t"%node)
            with open("../Draft Results COTILES/Merged.txt", 'r') as readfile2:
                for line2 in readfile2:
                    if line2.split()[0] == node:
                        writefile.write("%s\t"%(line2.split()[-1]))
