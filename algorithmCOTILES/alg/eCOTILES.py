# -*- coding: utf-8 -*-
"""
    Created on 20/07/2019
    @author: Nikolaos Sachpenderis
"""
import os

import networkx as nx
import datetime
import re
import time
import copy
from .COTILES import COTILES


import sys
if sys.version_info > (2, 7):
    from io import StringIO
else:
    from cStringIO import StringIO

__author__ = "Nikolaos Sachpenderis"
__contact__ = "sachpenderis@uom.edu.gr"
__website__ = "users.uom.gr/~sachpenderis/"
__license__ = "BSD"
# COTILES algorithm extends TILES in order to take into account the content of the network as well.
# TILES written by Giulio Rossetti (giulio.rossetti@gmail.com) can be found in https://github.com/GiulioRossetti/TILES


class eCOTILES(COTILES):
    """
        COTILES
        Algorithm for evolutionary community discovery with content handling
        ***Explicit removal***
    """

    def __init__(self, filename=None, g=nx.Graph(), obs=7, path="", start=None, end=None):
        """
            Constructor
            :param g: networkx graph
            :param obs: observation window (days)
            :param path: Path where generate the results and find the edge file
            :param start: starting date
            :param end: ending date
        """
        super(self.__class__, self).__init__(filename, g, 0, obs, path, start, end)

    def execute(self):
        """
            Execute TILES algorithm
        """
        self.status.write(u"Started! (%s) \n\n" % str(time.asctime(time.localtime(time.time()))))
        self.status.flush()

        with open("%s" % self.filename, 'r') as f:
            first_line = f.readline()

        actual_time = datetime.datetime.fromtimestamp(float(first_line.split()[3]))
        last_break = actual_time
        f.close()

        count = 0

        NetworkLabels = list()


        self.nodeLabels = {}
        self.nodeLabelPopularity = {}


        self.edgeLabels = {}



        #################################################
        #                   Main Cycle                  #
        #################################################


        f = open("%s" % self.filename)


        for l in f:
            l = l.rstrip().split("\t")
            self.added += 1
            e = {}
            action = l[0]

            if int(l[1])< int(l[2]):
                u = int(l[1])
                v = int(l[2])
            else:
                v = int(l[1])
                u = int(l[2])


            dt = datetime.datetime.fromtimestamp(float(l[3]))
            t = l[4]

            if action == '+':
                for lab in t.split(','):
                    NetworkLabels.append(lab)



                ########################################################################################################

                oldNodeLabels1 = self.nodeLabels.get(u)
                if oldNodeLabels1 != None:
                    newLabels1 = "%s,%s"%(oldNodeLabels1, t)
                else:
                    newLabels1 = "%s" % (t)


                labelsu = {u:  newLabels1}

                self.nodeLabels.update(labelsu)

                oldNodeLabels2 = self.nodeLabels.get(v)
                if oldNodeLabels2 != None:
                    newLabels2 = "%s,%s"%(oldNodeLabels2, t)
                else:
                    newLabels2 = "%s" % (t)

                labelsu = {v: newLabels2}
                self.nodeLabels.update(labelsu)

                ########################################################################################################


                #Calculate popularity of each node-label and node-labelset

                for j in self.nodeLabels.keys():
                    popularityCounter = 0
                    fraction = 0
                    for i in self.nodeLabels.get(j).split(','):
                        popularityCounter += NetworkLabels.count(i)
                        #frequencyOfLabelInNode = self.nodeLabels.get(j).split(',').count(i)
                        #relative_frequency = frequencyOfLabelInNode / len(self.nodeLabels.get(j).split(','))
                        #popularityCounter = relative_frequency * popularityCounter



                    fraction = popularityCounter / len(NetworkLabels)


                    thePopularity = {j: fraction}
                    self.nodeLabelPopularity.update(thePopularity)

                ####################################################################################################
                # EdgeLabelsList
                ####################################################################################################

                oldEdgeLabels = self.edgeLabels.get((u, v))
                if oldEdgeLabels != None:
                    newEdgeLabels = "%s,%s" % (oldEdgeLabels, t)
                else:
                    newEdgeLabels = "%s" % (t)
                edgelabels = {(u, v): newEdgeLabels}
                self.edgeLabels.update(edgelabels)
                ####################################################################################################

            e['weight'] = 1
            e["u"] = u
            e["v"] = v
            e['t'] = t







            edge = (u, v, t)



            #############################################
            #               Observations                #
            #############################################

            gap = dt - last_break
            dif = gap.days




            if dif >= self.obs:
                last_break = dt

                print("New slice. Starting Day: %s" % dt)

                self.status.write(u"Saving Slice %s: Starting %s ending %s - (%s)\n" %
                                  (self.actual_slice, actual_time, dt,
                                   str(time.asctime(time.localtime(time.time())))))

                self.status.write(u"Edge Added: %d\tEdge removed: %d\n" % (self.added, self.removed))
                self.added = 0
                self.removed = 0

                actual_time = dt
                self.status.flush()

                try:
                    os.mkdir("%s/%s/Draft Results COTILES/Splits" % (self.base, self.path))
                except:
                    pass
                self.splits = open(
                    "%s/%s/Draft Results COTILES/Splits/splitting-%d.txt" % (
                    self.base, self.path, self.actual_slice), "w")
                self.splits.write(self.spl.getvalue())
                self.splits.flush()
                self.splits.close()
                self.spl = StringIO()

                self.print_communities()
                self.status.write(
                    u"\nStarted Slice %s (%s)\n" % (self.actual_slice, str(datetime.datetime.now().time())))




            if u == v:
                continue

            # Check if edge removal is required
            try:
                if (action == '-'):
                    w = self.g.adj[u][v]["weight"]
                    self.g.adj[u][v]["weight"] = w - e['weight']

                    listofoldedgelabels = list()
                    listofnewedgelabels = list()
                    oldedgelabels = self.edgeLabels.get((u, v))
                    for o in oldedgelabels.split(','):
                        listofoldedgelabels.append(o)
                    newedgelabels = t
                    for p in newedgelabels.split(','):
                        listofnewedgelabels.append(p)
                    for m in listofnewedgelabels:
                        listofoldedgelabels.remove(m)

                    str1 = ""

                    # from string to list and again to string
                    for ele in listofoldedgelabels:
                        str1 += ele + ","

                    str1 = str1[:-1]

                    self.edgeLabels.update({(u, v): str1})






                    if self.g.adj[u][v]["weight"] == 0:
                        self.remove_edge(e)

                    else:
                        self.remove_tags_from_community(e)
                    continue
            except:
                pass


            if not self.g.has_node(u):
                self.g.add_node(u)
                self.g.node[u]['c_coms'] = {}

            if not self.g.has_node(v):
                self.g.add_node(v)
                self.g.node[v]['c_coms'] = {}

            if self.g.has_edge(u, v):
                w = self.g.adj[u][v]["weight"]
                self.g.adj[u][v]["weight"] = w + e['weight']
                #edgetags = self.g.adj[u][v]['t']
                # print(edgetags)
                #self.g.adj[u][v]["t"] = edgetags + "," + e['t']
                #oldedgelabels = self.edgeLabels.get((u, v))
                #newedgelabels = t
                #labelsforupdate = oldedgelabels +","+ newedgelabels
                #self.edgeLabels.update({(u, v): labelsforupdate})
                #continue
            else:
                self.g.add_edge(u, v, weight=e['weight'])
                #self.g.adj[u][v]["t"] = e['t']

            u_n = list(self.g.neighbors(u))
            v_n = list(self.g.neighbors(v))


            #############################################
            #               Evolution                   #
            #############################################

            # new community of peripheral nodes (new nodes)
            if len(u_n) > 1 and len(v_n) > 1:
                common_neighbors = set(u_n) & set(v_n)
                self.common_neighbors_analysis(u, v, common_neighbors, self.edgeLabels.get(u,v))

            count += 1



        #  Last writing


        self.status.write(u"Slice %s: Starting %s ending %s - (%s)\n" %
                          (self.actual_slice, actual_time, actual_time,
                           str(time.asctime(time.localtime(time.time())))))
        self.status.write(u"Edge Added: %d\tEdge removed: %d\n" % (self.added, self.removed))
        self.added = 0
        self.removed = 0




        self.print_communities()
        self.status.write(u"Finished! (%s)" % str(time.asctime(time.localtime(time.time()))))
        self.status.flush()
        self.status.close()




    def remove_edge(self, e):
        """
            Edge removal procedure
            :param actual_time: timestamp of the last inserted edge
            :param qr: Priority Queue containing the edges to be removed ordered by their timestamps
        """

        coms_to_change = {}

        self.removed += 1
        u = e["u"]
        v = e["v"]
        t = e["t"]
        edge = (u, v, t)

        if self.g.has_edge(u, v):

            # u and v shared communities
            if len(list(self.g.neighbors(u))) > 1 and len(list(self.g.neighbors(v))) > 1:
                coms = set(self.g.node[u]['c_coms'].keys()) & set(self.g.node[v]['c_coms'].keys())

                for c in coms:
                    if c not in coms_to_change:
                        cn = set(self.g.neighbors(u)) & set(self.g.neighbors(v))
                        coms_to_change[c] = [u, v]
                        coms_to_change[c].extend(list(cn))
                    else:
                        cn = set(self.g.neighbors(u)) & set(self.g.neighbors(v))
                        coms_to_change[c].extend(list(cn))
                        coms_to_change[c].extend([u, v])
                        ctc = set(coms_to_change[c])
                        coms_to_change[c] = list(ctc)
            else:
                if len(list(self.g.neighbors(u))) < 2:
                    coms_u = copy.copy(list(self.g.node[u]['c_coms'].keys()))
                    for cid in coms_u:
                        self.remove_from_community(u, cid, t)

                if len(list(self.g.neighbors(v))) < 2:
                    coms_v = copy.copy(list(self.g.node[v]['c_coms'].keys()))
                    for cid in coms_v:
                        self.remove_from_community(v, cid, t)

            self.g.remove_edge(u, v)

        # update of shared communities
        self.update_shared_coms(coms_to_change)

    def remove_tags_from_community(self, e):

        coms_to_change = {}

        u = e["u"]
        v = e["v"]
        t = e["t"]


        if self.g.has_edge(u, v):

            # u and v shared communities
            if len(list(self.g.neighbors(u))) > 1 and len(list(self.g.neighbors(v))) > 1:
                coms = set(self.g.node[u]['c_coms'].keys()) & set(self.g.node[v]['c_coms'].keys())
                for c in coms:
                    self.remove_expired_tags_from_community(u, c, t)
                    self.remove_expired_tags_from_community(v, c, t)
