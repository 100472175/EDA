from bst import BinarySearchTree
from bintree import BinaryNode


class BST2(BinarySearchTree):
    def isSameStructure(self, tree):
        if tree is None:
            return False
        if self.size() != tree.size():
            return False

        return self._isSameStructure(self._root, tree._root)

    def _isSameStructure(self, self_node, other_node):
        # Both are empty
        if self_node is None and other_node is None:
            return True

        # None of them are None, we compare them
        if self_node is not None and other_node is not None:
            return (self._isSameStructure(self_node.left, self_node.left) and
                    self._isSameStructure(self_node.right, self_node.right))

        # IF they are different, one is None and the other is not None
        return False


    def sumTree(self):
        sum = 0
        return self._sumTree(self._root, sum)


    def _sumTree(self, node, sum):
        if node is not None:
            # Recursion for right subtree
            sum = node.elem + self._sumTree(node.right, sum)
            # Recursion for the left subtree
            node.elem = sum - node.elem
            # Recursion for left subtree
            sum = self._sumTree(node.left, sum)

        return sum


    def lwc(self, a, b):
        nodeA = self.search(a)
        nodeB = self.search(b)
        if nodeA is None:
            return None
        if nodeB is None:
            return None

        trueroot = self._root
        self._lwc(nodeA, nodeB, self._root)
        lowest = self._root
        self._root = trueroot
        return lowest

    def _lwc(self, nodeA, nodeB, root):
        if root.left is not None:
            nodeL = root.left
        if root.right is not None:
            nodeR = root.right

        self._root = nodeL
        if self.search(nodeA) == nodeA:
            if self.search(nodeB) == nodeB:
                self._lwc(nodeA, nodeB, nodeL)
        self._root = nodeR
        if self.search(nodeA) == nodeA:
            if self.search(nodeB) == nodeB:
                self._lwc(nodeA, nodeB, nodeR)
        self._root = root




