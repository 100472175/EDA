from graph import AdjacentVertex
from graph import Graph
import sys


class Graph2(Graph):
    """def min_number_edges(self, start, end):
        # This function returns the minimum number of edges to navigate from the vertex start to the end vertex
        if start not in self._vertices or end not in self._vertices:
            raise ValueError("Vertex not in graph")
        if start == end:
            return 0
        disk = self.dijkstra(start)
        print("Dijkstra: ", disk)

        if end not in disk:
            return 0
            # raise ValueError("No path from start to end")

        if disk[end] == sys.maxsize:
            return 0
            # raise ValueError("No path from start to end")

        return disk[end]"""

    # Disktras Algorith with graphs
    """def dijkstra(self, start):
        # This function returns the minimum number of edges to navigate from the vertex start to the end verte"
        if start not in self._vertices:
            raise ValueError("Vertex not in graph")
        visited = {}
        for v in self._vertices.keys():
            visited[v] = False
        visited[start] = True
        distance = {}
        for v in self._vertices.keys():
            distance[v] = sys.maxsize
        distance[start] = 0
        queue = []
        queue.append(start)
        while queue:
            s = queue.pop(0)
            for adj in self._vertices[s]:
                if visited[adj.vertex] == False:
                    queue.append(adj.vertex)
                    visited[adj.vertex] = True
                    distance[adj.vertex] = distance[s] + 1
        return distance"""

    def min_number_edges(self, start, end):
        """ This function returns the minimum number of edges to navigate from the vertex start to the end vertex"""
        if start not in self._vertices or end not in self._vertices:
            raise ValueError("Vertex not in graph")
        if start == end:
            return 0
        visited = {}
        for v in self._vertices.keys():
            visited[v] = False
        visited[start] = True
        distance = {}
        for v in self._vertices.keys():
            distance[v] = sys.maxsize
        distance[start] = 0
        queue = [start]
        while queue:
            s = queue.pop(0)
            for adj in self._vertices[s]:
                if visited[adj.vertex] == False:
                    queue.append(adj.vertex)
                    visited[adj.vertex] = True
                    distance[adj.vertex] = distance[s] + 1
        if distance[end] == sys.maxsize:
            return 0
        return distance[end]

    #######################################################################################################################

    def is_strongly_connected(self) -> bool:
        """ This function checks if the graph is strongly connected.
        A directed graph is strongly connected when for any
        pair of vertices u and v, there is always a path from u to v.
        If the graph is undirected, the function returns True if the graph is
        connected, that is, there is a path from any vertex to any other vertex
        in the graph.
        """

        for i in self._vertices.keys():
            vis = self._bfs(i)
            for v in vis.items():
                if not v[-1]:
                    return False
        return True

    def _bfs(self, v):
        visited = {}
        for v in self._vertices.keys():
            visited[v] = False

        queue = []
        visited[v] = True
        queue.append(v)

        while queue:
            s = queue.pop(0)
            for adj in self._vertices[s]:
                if visited[adj.vertex] == False:
                    queue.append(adj.vertex)
                    visited[adj.vertex] = True

        return visited

    ######################################################################################################################

    def transpose(self) -> 'Graph2':
        """ returns a new graph that is the transpose graph of self, which is the graph with the edges reversed."""
        if not self._directed:
            return self
        else:
            new_graph = Graph2(self._vertices, self._directed)
            for i in self._vertices.keys():
                for j in self._vertices[i]:
                    new_graph.add_edge(j.vertex, i, j.weight)
            return new_graph


# self.vertices.keys() == ['A', 'B', 'C', 'D', 'E', 'F', 'G']
# self.vertices['A'] == [('B', 5), ('C', 2)]


if __name__ == "__main__":
    vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    t = Graph2(vertices)
    t.add_edge('A', 'B')
    t.add_edge('A', 'C')
    t.add_edge('B', 'C')
    t.add_edge('B', 'D')
    t.add_edge('C', 'E')
    t.add_edge('D', 'E')
    t.add_edge('E', 'F')
    t.add_edge('F', 'G')
    g = t.transpose()
    a = g.is_strongly_connected()
    print(a)
