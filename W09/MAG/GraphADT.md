#Chapter 6 - Graphs (Abstract data types)

- Properties
- Representation
- Graph traversal
- Shortest Path
<details> 
<summary> Introduction </summary> 
<p>
Non linear structure, consists of objects and relationships (edges)
Uses: Social Networks, as friend relationships or the street map or the subways metro map.
</p>
</details>

<details> 
<summary> Properties </summary> 
<p>
A graph G is an ordered pair of V vertices and a set of E edges <br>
 Types of edges: <br>
     1. Direct edges<br>
     2. Undirected edges<br>
     3. Parallel Edges (Try to avoid them)

Dense graph = #E ~ |V|**2
Sparse Graph = #E ~ |V|
</p>
</details>


## Adjacency Matrix
Python list to store the vertices, each vertex = list position, good to find the index of each vertex
Adjacency List  
When creating an adjacency matrix, finding adjacent nodes O(n) and winding if there is and edge O(1)

Path of 2 = Adjacent node of adjacent node.

<details> 
<summary> Graph Representation </summary> 
<p>
Conections of B can be: <br>
- Python lists
- Linked lists (we will use these)
</details>

Así le salen 92 diapositiva, porque hace una dispositiva en vez de hacer transiciones


