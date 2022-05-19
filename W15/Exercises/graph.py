# -*- coding: utf-8 -*-
import random


def compare_lists(list1: list, list2: list) -> bool:
    if len(list1) != len(list2):
        return False
    # we compare both list of vertices
    for a, b in zip(list1, list2):
        print(str(a), str(b))
        if a != b:
            return False
    return True


class AdjacentVertex:
    """ This class allows us to represent a tuple
    with an adjacent vertex
    and the weight associated (by default None, for non-unweighted graphs)"""

    def __init__(self, vertex: object, weight: int = 1) -> None:
        self.vertex = vertex
        self.weight = weight

    def __str__(self) -> str:
        """ returns the tuple (vertex, weight)"""
        return '(' + str(self.vertex) + ',' + str(self.weight) + ')'

    def __eq__(self, other) -> bool:
        if other is None:
            return False
        return self.vertex == other.vertex and self.weight == other.weight


class Graph:
    def __init__(self, vertices: list, directed: bool = True) -> None:
        """ We use a dictionary to represent the graph
        the dictionary's keys are the vertices
        The value associated for a given key will be the list of their neighbours.
        Initially, the list of neighbours is empty"""
        self._vertices = {}
        for v in vertices:
            self._vertices[v] = []
        self._directed = directed

    def add_edge(self, start: object, end: object, weight: int = 1) -> None:
        if start not in self._vertices.keys():
            print(start, ' does not exist!')
            return
        if end not in self._vertices.keys():
            print(end, ' does not exist!')
            return

        # adds to the end of the list of neighbours for start
        self._vertices[start].append(AdjacentVertex(end, weight))

        if not self._directed:
            # adds to the end of the list of neighbors for end
            self._vertices[end].append(AdjacentVertex(start, weight))

    def contain_edge(self, start: object, end: object) -> int:
        """ checks if the edge (start, end) exits. It does
        not exist return 0, eoc returns its weight or 1 (for unweighted graphs)"""
        if start not in self._vertices.keys():
            print(start, ' does not exist!')
            return 0
        if end not in self._vertices.keys():
            print(end, ' does not exist!')
            return 0

        # we search the AdjacentVertex whose v is equal to end
        for adj in self._vertices[start]:
            if adj.vertex == end:
                return adj.weight

        return 0  # does not exist

    def remove_edge(self, start: object, end: object):
        """ removes the edge (start, end)"""
        if start not in self._vertices.keys():
            print(start, ' does not exist!')
            return
        if end not in self._vertices.keys():
            print(end, ' does not exist!')
            return

        # we must look for the adjacent AdjacentVertex (neighbour)  whose vertex is end, and then remove it
        for adj in self._vertices[start]:
            if adj.vertex == end:
                self._vertices[start].remove(adj)
        if not self._directed:
            # we must also look for the AdjacentVertex (neighbour)  whose vertex is end, and then remove it
            for adj in self._vertices[end]:
                if adj.vertex == start:
                    self._vertices[end].remove(adj)

    def __str__(self) -> str:
        """ returns a string containing the graph"""
        result = ''
        for v in self._vertices:
            result += '\n' + str(v) + ':'
            for adj in self._vertices[v]:
                result += str(adj) + "  "
        return result

    def __eq__(self, other: 'Graph') -> bool:
        if other is None:
            return False

        if compare_lists(self._vertices, other._vertices):
            for v in self._vertices:
                print(v)
                if not compare_lists(self._vertices[v], other._vertices[v]):
                    return False
        return True


if __name__ == '__main__':
    # We use the class to represent an undirected graph without weights :
    # <img src='https://computersciencesource.files.wordpress.com/2010/05/dfs_1.png' width='35%'/>

    labels = ['A', 'B', 'C', 'D', 'E']
    g = Graph(labels, False)
    g.add_edge('A', 'B')  # A:0,  B:1
    g.add_edge('A', 'C')  # A:0,  C:2
    g.add_edge('A', 'E')  # A:0,  E:5
    g.add_edge('B', 'D')  # B:1,  D:4
    g.add_edge('B', 'E')  # C:2,  B:1
    # g.add_edge('A', 'H', 8)

    print(g)

    # Now,  we use the implementation to represent this graph:
    # <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/CPT-Graphs-directed-weighted-ex1.svg/722px-CPT-Graphs-directed-weighted-ex1.svg.png' width='25%'/>

    labels = ['A', 'B', 'C', 'D', 'E']
    g = Graph(labels)

    # Now, we add the edges
    g.add_edge('A', 'C', 12)  # A->(12)C
    g.add_edge('A', 'D', 60)  # A->(60)D
    g.add_edge('B', 'A', 10)  # B->(10)A
    g.add_edge('C', 'B', 20)  # C->(20)B
    g.add_edge('C', 'D', 32)  # C->(32)D
    g.add_edge('E', 'A', 7)  # E->(7)A

    print(g)
    print(g.contain_edge('C', 'B'))
    print(g.contain_edge('B', 'C'))
    g.remove_edge('C', 'B')
    print(g)
    g.remove_edge('A', 'D')
    print(g)


def quicksort(data):
    if len(data) < 2:
        return data
    else:
        pivot = data[0]
        less = [i for i in data[1:] if i <= pivot]
        greater = [i for i in data[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


"""def quickSortIn(data):
    indexes = [i for i in range(len(data))]
    return quicksortIndex(data, indexes)


def quicksortIndex(data, indexes):
    if len(data) < 2:
        return data
    else:
        pivot = data[0]
        less = []
        greater = []
        for i in indexes:
            if data[i] <= pivot:
                less.append(i)
            elif data[i] > pivot:
                greater.append(i)
        return quicksortIndex(data, less) + [data[0]] + quicksortIndex(data, greater)"""

data = [3, 0, 1, 8, 7, 2, 5, 4, 9, 6]
print(data)
print("QuickSort: ", quicksort(data))


# QuickSort con indices
def _quicksort(a: list, start: int, end: int) -> None:
    """La función ordena la sublista de a comprendida entre los índices start y end, ambos inclusives"""
    piv = a[end]
    i, j = start, end - 1
    while i <= j:
        # paramos de avanzar i, cuando encontramos un elemento a[i]>=p
        while a[i] < piv:
            i += 1
        # paramos de disminuir j, cuando encontramos un elemento a[j]<=p
        while a[j] > piv:
            j -= 1

        if i < j:
            # intercambiamos a[i], a[j]
            a[i], a[j] = a[j], a[i]
        """ if i <= j:
            i += 1
            j -= 1"""
    a[end], a[i] = a[i], a[end]
    if i - 1 > start:
        _quicksort(a, start, i - 1)
    if i + 1 < end:
        _quicksort(a, i + 1, end)


print("QuickSort con indices: ", quicksort(data))
print(_quicksort(data, 0, len(data) - 1))


def equicksort(array, start, end):
    if start >= end:
        return
    pivote = array[end]
    l, r = start, end - 1
    while 1 <= r:
        # print(l, r)
        while array[1] <= pivote:
            l += 1
            print(l, r)
        while array[r] >= pivote:
            r -= 1
        if r > l:
            array[l], array[r] = array[r], array[l]
    array[l], array[end] = array[end], array[l]
    _quicksort(array, start, r)
    _quicksort(array, l+1, end)


# MergeSort
def mergesort(data):
    if len(data) < 2:
        return data
    else:
        mid = len(data) // 2
        left = mergesort(data[:mid])
        right = mergesort(data[mid:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


data = [3, 0, 1, 8, 7, 2, 5, 4, 9, 6]
print(data)
print("Mergesort:", mergesort(data))
