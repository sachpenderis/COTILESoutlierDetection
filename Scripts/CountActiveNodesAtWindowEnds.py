

firstTimestamp = 1281458386
month = 60*60*24*30

nodes = set()
with open("../Datasets/NetworkUnix.txt", 'r') as readfile:
    for line in readfile:
        if int(line.split()[2]) < (firstTimestamp + month):
            nodes.add(int(line.split()[0]))
            nodes.add(int(line.split()[1]))
        else:
            print(len(nodes))
            firstTimestamp = int(line.split()[2])
            nodes.clear()