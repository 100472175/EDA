from graph import Graph

class Graph2(Graph):
    def get_adjacent(self, node) -> list:
        ...

    def get_origins(self, node) -> list:
        ...


    def non_accesible(self) -> list:
        ...

    def bfs(self, start) -> list:
        # Breadth traversal, that returns a dictionary, which contains the minimum number of jumps to reach each node
        ...

