import copy

class TwoBreakSorting:
    def chromosomeToCycle(self, chromosome):
        l = len(chromosome)
        nodes = [0]*(2*l)
        for j in range(l):
            i = chromosome[j]
            if i > 0:
                nodes[2*j] = 2*i-1
                nodes[2*j+1] = 2*i
            else:
                nodes[2*j] = -2*i
                nodes[2*j+1] = -2*i-1
        return nodes
        
    def cycleToChromosome(self, nodes):
        l = len(nodes) // 2
        chromosome = [0]*l
        for j in range(l):
            if nodes[2*j] < nodes[2*j+1]:
                chromosome[j] = nodes[2*j+1]//2
            else:
                chromosome[j] = -nodes[2*j]//2
        return chromosome

    def coloredEdges(self, genome):
        edges = set()
        for chromosome in genome:
            nodes = self.chromosomeToCycle(chromosome)
            nodes.append(nodes[0])
            for j in range(len(chromosome)):
                edges.add((nodes[2*j+1], nodes[2*j+2]))
        return edges
        
    def printGenome(self, genome):
        result = ''
        for chromosome in genome:
            result += '('+' '.join(['+'+str(e) if e>0 else str(e) for e in chromosome])+')'
        return result

    def twoBreakOnGraph(self, edges, i0, i1, j0, j1):
        edges.discard((i0, i1))
        edges.discard((i1, i0))
        edges.discard((j0, j1))
        edges.discard((j1, j0))
        edges.add((i0, j0))
        edges.add((i1, j1))
        return edges

    def groupNodes(self, edges):
        parent = dict()
        rank = dict()
        for e in edges:
            parent[e[0]] = e[0]
            parent[e[1]] = e[1]
            rank[e[0]] = 0
            rank[e[1]] = 0

        def findParent(i):
            if i != parent[i]:
                parent[i] = findParent(parent[i])
            return parent[i]
        
        def union(i, j):
            i_id = findParent(i)
            j_id = findParent(j)
            if i_id == j_id:
                return
            if rank[i_id] > rank[j_id]:
                parent[j_id] = i_id
            else:
                parent[i_id] = j_id
                if rank[i_id] == rank[j_id]:
                    rank[j_id] += 1
        
        def unionEdges(edge):
            union(edge[0], edge[1])
            if 1 == edge[0] % 2:
                union(edge[0], edge[0]+1)
            else:
                union(edge[0], edge[0]-1)

            if 1 == edge[1] % 2:
                union(edge[1], edge[1]+1)
            else:
                union(edge[1], edge[1]-1)

        for e in edges:
            unionEdges(e)

        nodesID = dict()
        nodesSets = set()

        for e in edges:
            id = findParent(e[0])
            nodesID[e[0]] = id
            nodesID[e[1]] = id
            nodesSets.add(id)
        
        return nodesSets, nodesID
    
    def buildEdgeDict(self, edges, nodesSet, nodesID):
        edgeDict = dict()
        for e in edges:
            id = nodesID[e[0]]
            if not id in edgeDict:
                edgeDict[id] = dict()
            edgeDict[id][e[0]] = e[1]
            edgeDict[id][e[1]] = e[0]
        return edgeDict
            
    def twoBreakOnGenome(self, genome, i0, i1, j0, j1):
        edges = self.twoBreakOnGraph(self.coloredEdges(genome), i0, i1, j0, j1)
        nodesSet, nodesID = self.groupNodes(edges)
        edgeDict = self.buildEdgeDict(edges, nodesSet, nodesID)
        nodesDict = dict()
        for id, eDict in edgeDict.items():
            nodesDict[id] = []
            currNode0 = list(eDict)[0]
            while len(eDict) > 0:
                nodesDict[id].append(currNode0)
                if 1 == currNode0 % 2:
                    currNode1 = currNode0+1
                else:
                    currNode1 = currNode0-1
                nodesDict[id].append(currNode1)
                newNode = eDict[currNode1]
                del eDict[currNode0]
                del eDict[currNode1]
                currNode0 = newNode
        newGenome = dict()
        for id, nodes in nodesDict.items():
            newGenome[id] = self.cycleToChromosome(nodes)
        newGenome = sorted(newGenome.values(), key = lambda x:abs(x[0]))
        return newGenome
    
    def edgeFromNontrivialCycle(self, edges, redEdges, blueEdges, blocks):
        parent = dict()
        rank = dict()
        for e in edges:
            parent[e[0]] = e[0]
            parent[e[1]] = e[1]
            rank[e[0]] = 0
            rank[e[1]] = 0

        def findParent(i):
            if i != parent[i]:
                parent[i] = findParent(parent[i])
            return parent[i]
        
        def union(i, j):
            i_id = findParent(i)
            j_id = findParent(j)
            if i_id == j_id:
                return
            if rank[i_id] > rank[j_id]:
                parent[j_id] = i_id
            else:
                parent[i_id] = j_id
                if rank[i_id] == rank[j_id]:
                    rank[j_id] += 1

        for e in edges:
            union(e[0], e[1])

        nodesID = dict()
        nodesSets = set()

        for e in edges:
            id = findParent(e[0])
            nodesID[e[0]] = id
            nodesID[e[1]] = id
            nodesSets.add(id)
        
        cycles = len(nodesSets)
        hasNontrivialCycle = False
        edge = None
        removedRedEdges = []
        if cycles != blocks:
            hasNontrivialCycle = True
            edgeDict = dict()
            redEdgeDict = dict()
            for e in edges:
                id = nodesID[e[0]]
                if not id in edgeDict:
                    edgeDict[id] = dict()
                edgeDict[id][e[0]] = e[1]
                edgeDict[id][e[1]] = e[0]
                if edge == None and len(edgeDict[id]) > 2 and e in blueEdges:
                    edge = (e[0], e[1])
                    edgeID = id
                if e in redEdges:
                    if not id in redEdgeDict:
                        redEdgeDict[id] = dict()
                    redEdgeDict[id][e[0]] = e[1]
                    redEdgeDict[id][e[1]] = e[0]
            removedRedEdges.append((edge[0], redEdgeDict[edgeID][edge[0]]))
            removedRedEdges.append((edge[1], redEdgeDict[edgeID][edge[1]]))
        return hasNontrivialCycle, removedRedEdges        

    def shortestRearrangement(self, P, Q):
        blocks = sum([len(a) for a in P])
        result = [P]
        redEdges = self.coloredEdges(P)
        blueEdges = self.coloredEdges(Q)
        breakpointGraph = redEdges.union(blueEdges)
        hasNontrivialCycle, removedRedEdges = self.edgeFromNontrivialCycle(breakpointGraph, redEdges, blueEdges, blocks)
        while hasNontrivialCycle:
            redEdges = self.twoBreakOnGraph(redEdges, removedRedEdges[0][0], removedRedEdges[0][1], removedRedEdges[1][0], removedRedEdges[1][1])
            breakpointGraph = redEdges.union(blueEdges)
            P = self.twoBreakOnGenome(P, removedRedEdges[0][0], removedRedEdges[0][1], removedRedEdges[1][0], removedRedEdges[1][1])
            hasNontrivialCycle, removedRedEdges = self.edgeFromNontrivialCycle(breakpointGraph, redEdges, blueEdges, blocks)
            result.append(P)
        return result


if __name__ == "__main__":
    sorter = TwoBreakSorting()

    # Hardcoded input genomes
    P = [[+9, +12, +1, +14, -2, +11, -8, +6, -4, +5, -10, -3, -15, +13, +7]]
    Q = [[+4, -15, -10, +7, +8, -14, +2, +12, -9, -13, -3, -11, -5, +1, -6]]

    result = sorter.shortestRearrangement(P, Q)

    for r in result:
        print(sorter.printGenome(r))