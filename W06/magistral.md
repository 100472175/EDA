# Hierarchical data
## Non linear data structure

Pre order traversal
```
F, D, B, A, C, E, J, G, I, H, K
```

Post order traversal < left> < right> root:
```
A, C, B, E, D, H, I, G, K, J, F
```

In-Order traversal < right> root < left>
```
A, B, C, D, E, F, G, H, I, J, K
```

Level order traversal Por orden de arriba a abajo, de izq a derecha
```
F, D, J, B, E, G, K, A, C, I, H
```

How to implement trees in python 3 => using two classes:

````python
class SNode:
    def __init__(self, element, left=None, right=None, parent=None):
        self.parent = parent
        self.left = left
        self.right = right
        self.elem = element


class BinaryTree:
    def __init__(self):
        # Creates an empty binary tree
        self._root = None

    def size(self):
        """Returns the number of nodes in the tree"""
        return self._size(self._root)

    def _size(self, node):
        """Returns the size of the subtree from a specific node"""
        if node is None:
            return 0
        return 1 + self._size(node.left) + self._size(node.right)

    def height(self):
        return self._height(self._root)

    def _height(self, node):
        if node is None:
            return -1
        return 1 + max(self._height(node.left), self._height(node.right))

    def depth(self, node):
        """No me ha dado tiempo"""

class BinarySearchTree(BinaryTree):
    """WIll be used in the future, but the importat part is that it inherits the class BinaryTree"""
````

Pre-Order travesal implementation in python:
````python
class BinaryTree:
    def preorder(self):
        self._preorder(self.root)

    def _preorder(self, node):
        if node is not None:
            print(node.elem)
            self.preorder(node.left)
            self.preorder(node.right)

````
