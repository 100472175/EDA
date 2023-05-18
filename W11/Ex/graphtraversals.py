# -*- coding: utf-8 -*-
"""GraphTraversals.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DUsjyfrn2aP4RPoHf-MGgNlYVBfcXZ8d

# Graph traversals

First, we need to load a python file containing the implementation of a graph (graphdictionarywd.py).

You can download from
https://github.com/isegura/EDA/blob/master/graph.py

There are some online tools that can help you to represent and see how the traversal works on a graph:

- https://visualgo.net/en/dfsbfs?slide=1
- https://graphonline.ru/en/

They are really good!!!
"""


"""## Breadth First Search


"""

from graph import Graph


class Graph2(Graph):

    def bfs(self):
        """This functions prints all vertices of the graph by BFS traversal"""
        print('bfs traversal:')
        # Mark all the vertices as not visited 
        visited={}
        for v in self._vertices.keys():
            visited[v]=False

        for v in self._vertices.keys():
            if visited[v]==False:
                self._bfs(v,visited)

    # Function to print a BFS of graph 
    def _bfs(self, v,visited): 
        """This functions obtains the BFS traversal from the vertex 
        whose index is indexV."""
        
        # Create a queue for BFS. It will save the indices of vertices to visit
        queue = [] 
        #mark the source vertex as visited 
        visited[v] = True
        # and enqueue it 
        queue.append(v)
        
        while queue: 
            # Dequeue an index from queue and print its corresponding vertex(label)
            s = queue.pop(0) 
            #print (s, end = " ") 
            #we print the vertex, so we need to get its label
            print (s, end = " ") 

            # Get all adjacent vertices of the dequeued index. 
            # If an adjacent vertex has not been visited, 
            # then mark it visited and enqueue it 
            for adj in self._vertices[s]: 
                if visited[adj.vertex] == False:
                    queue.append(adj.vertex)
                    visited[adj.vertex] = True

  # The function to do DFS traversal. It uses recurison
    def dfs(self):
        """This function prints all vertices of the graph by the DFS traversal."""
    
        print('dfs traversal:')
        # Mark all the vertices as not visited
        visited={}
        for v in self._vertices.keys():
            visited[v]=False

        for v in  self._vertices.keys():
            if visited[v]==False:
              self._dfs(v, visited)
        print()



    def _dfs(self, v, visited):
        """This funcion prints the DFS traversal from the vertex whose index is indexV"""
        # Mark the current node as visited and print it
        visited[v] = True
        #print(v, end = ' ')
        #Instead of printing the index, we have to print its label
        print(v,end=' ')
        # Recur for all the vertices  adjacent to this vertex
        for adj in self._vertices[v]:
          if visited[adj._vertex] == False:
            self._dfs(adj._vertex, visited)

"""Now, we use the implementation to represent and trasverse this graph: 

<img src='https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/CPT-Graphs-directed-weighted-ex1.svg/722px-CPT-Graphs-directed-weighted-ex1.svg.png' width='25%'/>
"""


#we use this dictionary to represent the vertices with numbers:
if __name__ == '__main__':

    labels=['A','B','C','D','E']

    g=Graph2(labels)

    #Now, we add the edges
    g.add_edge('A','C',12) #A->(12)C
    g.add_edge('A','D',60) #A->(60)D
    g.add_edge('B','A',10) #B->(10)A
    g.add_edge('C','B',20) #C->(20)B
    g.add_edge('C','D',32) #C->(32)D
    g.add_edge('E','A',7)  #E->(7)A

    print(g)
    print()

    g.bfs()
    print()

    label='C'
    # Mark all the vertices as not visited 
    visited={}
    for v in labels:
        visited[v]=False

    print('bfs traversal from ', label)
    #we have to pass the index of the vertex 
    g._bfs(label,visited)
    print()

    label='E'
    visited={}
    for v in labels:
        visited[v]=False
    print('bfs traversal from ', label)
    #we have to pass the index of the vertex 
    g._bfs(label,visited)

    """We use the implementation to represent an undirected graph without weights :


    <img src='https://computersciencesource.files.wordpress.com/2010/05/dfs_1.png' width='35%'/>
    """

    labels=['A','B','C','D','E']
    g=Graph2(labels,False)
    g.addEdge('A','B') # A:0, B:1
    g.addEdge('A','C') # A:0, C:2
    g.addEdge('A','E') # A:0, E:5
    g.addEdge('B','D') # B:1, D:4
    g.addEdge('B','E') # C:2, B:1
    #g.addEdge('A','H',8)

    print(g)

    print('bfs traversal from A (A is the first vertex):')
    g.bfs()
    print()
    label='E'
    visited={}
    for v in labels:
        visited[v]=False
    print('bfs traversal from ', label)
    #we have to pass the index of the vertex 
    g._bfs(label,visited)

    """## Depth First Search


    """
    #we use this dictionary to represent the vertices with numbers:
    labels=['A','B','C','D','E']

    g=Graph2(labels)

    #Now, we add the edges
    g.addEdge('A','C',12) #A->(12)C
    g.addEdge('A','D',60) #A->(60)D
    g.addEdge('B','A',10) #B->(10)A
    g.addEdge('C','B',20) #C->(20)B
    g.addEdge('C','D',32) #C->(32)D
    g.addEdge('E','A',7)  #E->(7)A

    print(g)
    print()

    g.dfs()
    print()

    visited={}
    for v in labels:
        visited[v]=False
    print('dfs traversal from B')
    g._dfs('B',visited)