
with open ("../Draft Results COTILES/MergedPopularity.txt", 'a') as writefile:
    for i in range (110):
        with open("../Draft Results COTILES/LabelSet Popularity/popularity-%s.csv"%i, 'r') as readfile:
            for line in readfile:
                writefile.write(line)
