from graph import Graph


class Graph2(Graph):
    def get_adjacents(self, v: object) -> object:
        """ returns the list of adjacents of vertex"""
        if v not in self._vertices.keys():
            print(v, ' does not exist!')
            return
        return self._vertices[v]

    def get_origins(self, v):
        """ returns the list of origins of vertex"""
        if v not in self._vertices.keys():
            print(v, ' does not exist!')
            return None
        verts = []
        for adj in self._vertices.values():
            for elem in adj:
                if elem.vertex == v:
                    verts.append(adj)
        return verts

    def non_accesible(self, v):
        """ returns the list of non accesible vertices"""
        if v not in self._vertices.keys():
            print(v, ' does not exist!')
            return None
        visited = {}
        for v1 in self._vertices:
            visited[v1] = False
        self._dfs(v, visited)

        unaccesible_verts = []
        for v2 in self._vertices:
            if not visited[v2]:
                unaccesible_verts.append(v2)

        return unaccesible_verts

    def _dfs(self, v: str, visited: dict):
        visited[v] = True
        for adj in self._vertices[v]:
            if not visited[adj.vertex]:
                self._dfs(adj.vertex, visited)


if __name__ == '__main__':
    vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    directed_graph = Graph2(vertices)
    directed_graph.add_edge('A', 'B')
    directed_graph.add_edge('A', 'C')
    directed_graph.add_edge('B', 'C')
    directed_graph.add_edge('B', 'D')
    directed_graph.add_edge('C', 'E')
    directed_graph.add_edge('D', 'E')
    directed_graph.add_edge('E', 'F')
    directed_graph.add_edge('F', 'G')
    print(directed_graph)
    a = directed_graph.get_origins('B')
    a = a[0]
    for i in range(len(a)):
        print(a[i])
