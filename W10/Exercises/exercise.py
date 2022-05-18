import timeit

# Look inorder and Inorder List
dic = {}
print(dic)
dic = {1: 'a', 2: "2", "yes": "si"}
dic[5] = 'D'
print(dic.keys())
print(dic.values())
print(dic.items())

graph = {'A': ['B', 'C'], 'B': ['A', 'B', 'E'], 'C': ['A', 'F'], 'D': ['B', 'E'], 'E': ['B', 'D'], 'F': ['C']}
print(graph)
graph = {}
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'B', 'E']


graph_adj = {}
graph_adj['A'] = [('B', 5), ('C', 1)]
graph_adj['B'] = [('A', 5), ('C', 8), ('D', 6)]
graph_adj['C'] = [('A', 1), ('B', 8)]
graph_adj['D'] = [('B', 6)]



