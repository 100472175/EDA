# Python3 program to count non-reachable
# nodes from a given source using DFS.

# Graph class represents a directed graph
# using adjacency list representation
class Graph:
    def __init__(self, V):
        self.v = V
        self.adj = [[] for i in range(V)]

    def addEdge(self, v, w):
        self.adj[v].append(w) # We only eneed one, as it is directed
        # self.adj[w].append(v)

    def DFSUtil(self, v, visited):
        # Mark the current node as visited
        # and print it
        visited[v] = True
        # Recur for all the vertices
        # adjacent to this vertex
        for i in self.adj[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)
        return visited

    # Returns count of not reachable
    # nodes from vertex v.
    # It uses recursive DFSUtil()
    def countNotReach(self, v):
        verts = {}
        # visited = [False] * self.V
        # Mark all the vertices as not visited
        for i in range(len(self.adj)):
            verts[i] = False
        verts = self.DFSUtil(v, verts)
        count = 0
        for i in verts:
            if verts[i] is False:
                count += 1
        return count


# Driver Code
if __name__ == '__main__':
    # Create a graph given in the
    # above diagram
    g = Graph(8)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(3, 4)
    g.addEdge(4, 5)
    g.addEdge(6, 7)

    print(g.countNotReach(1))

# This code is contributed by PranchalK
