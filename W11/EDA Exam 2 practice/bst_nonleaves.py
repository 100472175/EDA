"""
# Problem 1 - Binary Search Trees

In a binary tree, a non-leaf node is a node that has at least one child.

Let MyBST be the class that implements a binary search tree (actually it is a simplified version that only includes the
methods needed to create and populate a tree).
Implement a method, **getNonLeaves()**, which returns a Python list containing the elements of non-leaf nodes.
The list must be sorted in descending order (highest to lowest).
"""


class Node:
    def __init__(self, elem, left=None, right=None, parent=None):
        self.elem = elem
        self.left = left
        self.right = right
        self.parent = parent


class MyBST:
    def __init__(self):
        self.root = None

    def insert(self, x):
        """inserts a new node, with element x, into the tree"""
        if self.root == None:
            self.root = Node(x)
        else:
            self._insertNode(self.root, x)

    def _insertNode(self, node, x):
        """método recursivo"""
        if node.elem == x:
            # print('Error: la clave ya existe. No permitimos duplicados')
            return

        if x < node.elem:

            if node.left == None:
                # ya he encontrado su sitio
                newNode = Node(x)
                newNode.parent = node
                node.left = newNode
            else:
                self._insertNode(node.left, x)

        else:  # x>node.elem

            if node.right == None:
                # ya he encontrado la posición
                newNode = Node(x)
                newNode.parent = node
                node.right = newNode
            else:
                self._insertNode(node.right, x)

    def draw(self):
        """Function to draw the tree"""
        self._draw('', self.root, False)
        print()

    def _draw(self, prefix, node, isLeft):
        if node != None:
            self._draw(prefix + "     ", node.right, False)
            print(prefix + ("|-- ") + str(node.elem))
            self._draw(prefix + "     ", node.left, True)

    def getNonLeaves(self):
        ...


import unittest


class Test(unittest.TestCase):
    # variable estática para almacenar la nota
    nota = 0

    def setUp(self):
        values = [25, 20, 36, 10, 22, 30, 40, 5, 12, 28, 38, 48]
        self.bst1 = MyBST()
        for x in values:
            self.bst1.insert(x)

        # self.bst1.draw()

        values = [12, 16, 19, 20, 4, 14, 2, 18, 10, 8, 24, 6, 1, 13]
        self.bst2 = MyBST()
        for x in values:
            self.bst2.insert(x)

        # self.bst2.draw()

    def test_printNota(self):
        print('\n\n*************************')
        print("\nNota Final:", Test.nota)
        print('*************************')

    def test1_getNonLeaves(self):
        print('Case 1: tree is empty')
        tree = MyBST()
        self.assertEqual(len(tree.getNonLeaves()), 0, "Fail: list should be empty")
        print('\t\t nota += 1')
        Test.nota += 1

    def test2_getNonLeaves(self):
        print('Case 2: tree only has one node')
        tree = MyBST()
        tree.insert(10)
        self.assertEqual(len(tree.getNonLeaves()), 0, "Fail: list should be empty")
        print('\t\t nota += 2')
        Test.nota += 2

    def test3_getNonLeaves(self):
        print('Case 3: tree only has two nodes')
        tree = MyBST()
        tree.insert(10)
        tree.insert(15)
        result = tree.getNonLeaves()
        print('result:  ', result)
        expected = [10]
        print('expected:  ', expected)
        self.assertListEqual(result, expected, "Fail: list should be [10]")
        print('\t\t nota += 1')
        Test.nota += 1

    def test4_getNonLeaves(self):
        print('Case 4: tree only has three nodes and no left subtree')
        tree = MyBST()
        tree.insert(10)
        tree.insert(15)
        tree.insert(20)
        result = tree.getNonLeaves()
        print('result:  ', result)
        expected = [15, 10]
        print('expected:  ', expected)
        self.assertListEqual(result, expected, "Fail: list should be [15,10]")
        print('\t\t nota += 2')
        Test.nota += 2

    def test5_getNonLeaves(self):
        print('Case 5: tree only has three nodes and no right subtree')
        tree = MyBST()
        tree.insert(20)
        tree.insert(15)
        tree.insert(10)
        result = tree.getNonLeaves()
        print('result:  ', result)
        expected = [20, 15]
        print('expected:  ', expected)
        self.assertListEqual(result, expected, "Fail: list should be [20,15]")
        print('\t\t nota += 2')
        Test.nota += 2

    def test6_getNonLeaves(self):
        print('Case 6: tree is balanced and only has three nodes')
        tree = MyBST()
        tree.insert(15)
        tree.insert(10)
        tree.insert(20)
        result = tree.getNonLeaves()
        print('result:  ', result)
        expected = [15]
        print('expected:  ', expected)
        self.assertListEqual(result, expected, "Fail: list should be [10]")
        print('\t\t nota += 2')
        Test.nota += 2

    def test7_getNonLeaves(self):
        print('Case 7: tree only has two nodes')
        result = self.bst1.getNonLeaves()
        print('result:  ', result)
        expected = [40, 36, 30, 25, 20, 10]
        print('expected:  ', expected)
        self.assertListEqual(result, expected, "Fail: list should be [40, 36, 30, 25, 20, 10]")
        print('\t\t nota += 5')
        Test.nota += 5

    def test8_getNonLeaves(self):
        print('Case 7: tree only has two nodes')
        result = self.bst2.getNonLeaves()
        print('result:  ', result)
        expected = [20, 19, 16, 14, 12, 10, 8, 4, 2]
        print('expected:  ', expected)
        self.assertListEqual(result, expected, "Fail: list should be [20, 19, 16, 14, 12, 10, 8, 4, 2]")
        print('\t\t nota += 5')
        Test.nota += 5

    # Comentar para usarlo en spyder


unittest.main(argv=['first-arg-is-ignored'], exit=False)

# Descomenar para usarlo en Spyder
# if __name__ == '__main__':
#    unittest.main()
