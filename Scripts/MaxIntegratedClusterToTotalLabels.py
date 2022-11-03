import networkx

l = set()
with open("../Results Stats 1510/CommunitiesOnlyMembers/strong-communities-0.txt", 'r') as readfile:
    for line in readfile:
        for node in line.split(','):
            l.add(int(node))


G = networkx.MultiGraph()
with open("../Results Stats 1510/Graph/graph-0.txt", 'r') as readfile2:
    for line in readfile2:
        for weight in range (int(line.split()[2])):
            u = line.split()[0]
            v = line.split()[1]

            G.add_edge(u,v)



with open("../Results Stats 1510/MaxIntegratedInClusterToTotalLabels.txt", 'w') as writefile:
    with open("../Results Stats 1510/Nodes' Labels/nodesLabels-0.csv", 'r') as readLabels:

        for linel in readLabels:
            nodel = linel.split()[0]
            s = set()
            for labelset in linel.split()[2:]:
                for label in labelset.split(','):
                    s.add(label)
            print(s)
            contentScore = 0
            totalLabelCounter = 0
            inClusterLabelCounter = 0
            with open("../Results Stats 1510/CommunitiesLabels/strong-communities-0.txt", 'r') as readComLabels:
                for line in readComLabels:
                    communityLabels = set()
                    for label in line.split(','):
                        communityLabels.add(str(label.strip(" , \n")))
                    print(communityLabels)

                    intersection = s&communityLabels
                    print(intersection)

                    score = len(intersection)/len(communityLabels)

                    if score> contentScore:
                        contentScore = score
                writefile.write("%s\t%s\t%s\t%.2f\n"%(nodel, len(s), int(nodel) in l, contentScore))
