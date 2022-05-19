from graph import AdjacentVertex
from graph import Graph
import sys
import math


class Graph2(Graph):

    def min_number_edges(self, start: str, end: str) -> int:
        """returns the minimum number of edges from start to end"""
        nodes = self._vertices.keys()
        if start not in nodes or end not in nodes:
            print("no se pueden buscar caminos entre vértices que no existen")
            return -1

        visited = {}
        distances = {}

        for _ in nodes:
            visited[_] = False
            distances[_] = math.inf
        distances[start] = 0
        visited[start] = True

        i = start
        while not visited[end]:
            children = []
            for _ in self._vertices[i]:
                if not visited[_.vertex]:
                    children.append(_.vertex)

            # si es > 0 hemos llegado a un vértice terminal, no podremos continuar
            if len(children) > 0:
                for j in children:

                    distance = distances[i]
                    if distances[j] > distance + 1:
                        distances[j] = distance + 1
                lowest = children[0]

                # elegimos el siguiente nodo a evaluar
                for k in children:
                    if distances[k] < distances[lowest]:
                        lowest = k
                i = lowest
                visited[lowest] = True
            else:
                return 0

        """if distances[end] == math.inf:
            distances[end] = 0"""
        return distances[end]



    def dijkstra(self, start: str) -> dict:
        """ This function returns a dictionary with the shortest path from start to all other vertices in the graph.
        The dictionary's keys are the vertices
        The value associated for a given key will be the list of their neighbours.
        Initially, the list of neighbours is empty"""
        if start not in self._vertices.keys():
            raise ValueError("Vertex not in graph")
        visited = {}
        for v in self._vertices.keys():
            visited[v] = False
        queue = []
        visited[start] = True
        queue.append(start)
        dist = {}
        for v in self._vertices.keys():
            dist[v] = sys.maxsize
        dist[start] = 0
        while queue:
            s = queue.pop(0)
            for adj in self._vertices[s]:
                if visited[adj.vertex] == False:
                    queue.append(adj.vertex)
                    visited[adj.vertex] = True
                    dist[adj.vertex] = dist[s] + adj.weight
        return dist


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

#######################################################################################################################

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
