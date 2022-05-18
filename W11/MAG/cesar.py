from bst import BinarySearchTree
import sys
import time


class BST2(BinarySearchTree):
    # Problem 1
    def primos(self, a, b):
        parentA = self.get_parent(a)
        parentB = self.get_parent(b)
        if parentA == parentB:
            return False
        elif self.get_parent(parentA.elem) == self.get_parent(parentB.elem):
            return True
        else:
            return False

    def get_parent(self, e):
        node_it = self._root
        prev = None
        while node_it.elem != e and node_it is not None:
            prev = node_it
            if node_it.elem < e:
                node_it = node_it.right
            elif node_it.elem > e:
                node_it = node_it.left
            else:
                return prev.elem
        return None

    # Problem 2 Edu
    def lowest_common_ancestor(self, a, b):
        nodeA = self.search(a)
        if nodeA is None:
            return None

        nodeB = self.search(b)
        if nodeB is None:
            return None

        return self._lwc(self._root, a, b)

    def _lwc(self, node, a, b):
        if node is None:
            return None
        if a < node.elem and b < node.elem:
            return self._lwc(node.left, a, b)
        elif a > node.elem and b > node.elem:
            return self._lwc(node.right, a, b)
        else:
            return node.elem

    # Problem 2 Cesar
    def lwcCesar(self, a, b):
        node_a = self.search(a)
        node_b = self.search(b)
        if node_a is None or node_b is None:
            print("uno de los nodos no existe", end=': ')
            return None
        if a > b:
            # los ordenamos para que a siempre sea menor que b
            a, b = b, a
            node_a, node_b = node_b, node_a
        bolean1 = self.is_descendence(node_a, node_b)
        bolean2 = self.is_descendence(node_b, node_a)
        return self._lwcCesar(self._root, a, b, bolean1, bolean2)

    def _lwcCesar(self, root, a, b, boolean1, boolean2):
        # un nodo será ancestro común de otros dos nodos si dicho nodo es mayor que node_a y menor de node_b
        if root is None:
            return None
        if not boolean2 and not boolean1:
            if a < root.elem < b:
                return root.elem
            if b < root.elem:
                return self._lwcCesar(root.left, a, b, False, False)
            if a > root.elem:
                return self._lwcCesar(root.right, a, b, False, False)
        elif boolean1:
            return self.get_parent(a)
        else:
            return self.get_parent(b)

    def is_descendence(self, node, node2) -> bool:
        if node2 == self._search(node, node2.elem):
            return True
        return False


    # Problem 3
    def is_zigzag(self):
        return self._iszigzag(self._root, "a")

    def _iszigzag(self, node, n):
        print(n)
        if node.left is None and node.right is None:
            return True
        elif node.right is not None and node.left is not None:
            return False
        if n == "a":
            if node.left is None and node.right is not None:
                return self._iszigzag(node.right, 0)
            elif node.right is None and node.left is not None:
                return self._iszigzag(node.left, 1)
        elif n == 1:
            if node.left is None and node.right is not None:
                return self._iszigzag(node.right, 0)
        elif n == 0:
            if node.left is not None and node.right is None:
                return self._iszigzag(node.left, 1)
        return False

    # Problem 4 Edu
    def is_left_odd_right_even(self):
        return self._is_left_odd_right_even(self._root)

    def _is_left_odd_right_even(self, node):
        if node.left is not None and node.right is not None:
            if node.left.left is not None and node.left.right:
                if self.is_odd(node.left.elem):
                    return self._is_left_odd_right_even(node.left.left) and \
                           self._is_left_odd_right_even(node.right.right)
            if node.right.left is not None and node.right.right:
                if self.is_even(node.right.elem):
                    return self._is_left_odd_right_even(node.left) and \
                           self._is_left_odd_right_even(node.right)

    def is_odd(self, elem):
        if elem % 2 != 0:
            return True
        return False

    def is_even(self, elem):
        if elem % 2 == 0:
            return True
        return False

    # Problem 5
    def isSameStructure(self, tree):
        return self._isSameStructure(self._root, tree._root)

    def _isSameStructure(self, a, b):
        if a is None and b is None:
            return True

        if a is not None and b is not None:
            return self._isSameStructure(a.left, b.left) and self._isSameStructure(a.right, b.right)

        return False

    # Problem 6 
    def closest(self, num) -> int:
        max = self._root
        while max.right is not None:
            max = max.right
        if num > max.elem:
            return max

        min = self._root
        while min.left is not None:
            node = min.left
        if num < min.elem:
            return min

        if self.search(num):
            return num
        for i in range(sys.maxsize):
            i += 1
            if self.search(num + i):
                return num + i
            elif self.search(num - i):
                return num - i

    # Problem 9
    def get_non_leaves(self):
        result = []
        self._get_non_leaves(self._root, result)
        return result

    def _get_non_leaves(self, node, lista):
        if node.right is None and node.left is None:
            return None
        self._get_non_leaves(node.right, lista)
        lista.append(node.elem)
        self._get_non_leaves(node.left, lista)

   # Problema Extra
    def isBST(self):
        return self._isBST(self._root)

    def _isBST(self, node):
        if node is None:
            return True
        condition1 = True
        condition2 = True
        if node.right:
            condition1 = node.right.elem > node.elem
        if node.left:
            condition2 = node.left.elem < node.elem

        return condition1 and condition2 and self._isBST(node.right) and self._isBST(node.left)


# Problem 10
def array2bst(array):
    tree = BST2()
    if len(array) == 0:
        return tree
    tree = _array2bst(array, tree)
    # tree.insert(array[0])
    return tree


def _array2bst(array: list, tree):
    half = (len(array) - 1) // 2
    if len(array) > 0:
        tree.insert(array[half])
        _array2bst(array[:half], tree)
        _array2bst(array[half + 1:], tree)
    return tree


# Problem 10 sin slicing
def array2bst_noslicing(array):
    arbol = BST2()
    return _array2bst2(arbol, array, 0, len(array) - 1)


def _array2bst2(arbol, array, inicio, final):
    middle = (final - inicio) // 2 + inicio
    if inicio <= final:
        # print(array[middle])
        arbol.insert(array[middle])
        _array2bst2(arbol, array, inicio, middle - 1)
        _array2bst2(arbol, array, middle + 1, final)
    return arbol


"""a = [1, 2, 3, 4, 5]
b = array2bst_noslicing(a)
b.draw()"""

"""a = []
for i in range(21):
    a.append(i + 1)

b = array2bst(a)
b.draw()"""
b = BST2()
a = [1, 3, 9, 27, 29, 37, 43, 51, 53, 59, 61, 67, 71, 73, 79, 83]

for i in a:
    b.insert(i)
b.insert(int(1e6))
b.insert(int(-1e6))

"""print("holo")
z = time.time()
print(b.closest((1e6 + 15)//2))
zz = time.time()
print("Ha tardado", zz-z)"""
