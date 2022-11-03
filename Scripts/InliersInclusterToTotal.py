import networkx
'''
l = set()
with open("../Draft Results COTILES/CommunitiesOnlyMembers/strong-communities-0.txt", 'r') as readfile:
    for line in readfile:
        for node in line.split(','):
            l.add(int(node))

print(l)'''

G = networkx.MultiGraph()
with open("../Results Stats 1510/Graph/graph-0.txt", 'r') as readfile2:
    for line in readfile2:
        for weight in range (int(line.split()[2])):
            u = line.split()[0]
            v = line.split()[1]

            G.add_edge(u,v)



with open("../Results Stats 1510/InClusterToTotal.txt", 'w') as writefile:
    with open("../Results Stats 1510/CommunitiesOnlyMembers/strong-communities-0.txt", 'r') as readfile:
        for line in readfile:
            community = list()
            for node in line.split(','):
                community.append(int(node))

            for n in community:
                totalEdgeCounter = 0
                inClusterEdgeCounter = 0
                with open("../Results Stats 1510/Graph/graph-0.txt", 'r') as readfile3:
                    for line3 in readfile3:
                        if int(n) == int(line3.split()[0]) :
                            totalEdgeCounter += (int(line3.split()[2]))
                            if int(line3.split()[1]) in community:
                                inClusterEdgeCounter += (int(line3.split()[2]))

                        if int(n) == int(line3.split()[1]):
                            totalEdgeCounter += (int(line3.split()[2]))
                            if int(line3.split()[0]) in community:
                                inClusterEdgeCounter += (int(line3.split()[2]))
                writefile.write("%s\t%s\t%s\t%.2f\n"%(n, inClusterEdgeCounter, totalEdgeCounter, inClusterEdgeCounter/totalEdgeCounter))
