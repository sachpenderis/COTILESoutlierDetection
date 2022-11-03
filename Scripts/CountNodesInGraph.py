
#for ttl in (30,45):
ttl=30
for i in range(0,100):
    nodes = set()
    members = set()
    with open ("../ResultsUnixEtiles%s30/Graph/graph-%s.txt"%(ttl,i), 'r') as readfile:
        for line in readfile:
            nodes.add(int(line.split()[0]))
            nodes.add(int(line.split()[1]))

    with open ("../ResultsEtiles%s30/CommunitiesMembers/strong-communities-%s.txt"%(ttl,i), 'r') as readfile2:
        for line2 in readfile2:
            for n in line2.split(','):
                members.add(int(n))


    print(nodes)
    print(members)
    print(len(nodes))
    print(len(members))
    print(len(members)/ len(nodes))
