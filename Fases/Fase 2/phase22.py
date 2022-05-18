# from binarysearchtree import BinarySearchTree
from bst import BinarySearchTree
from bst import BinaryNode
import sys

sys.setrecursionlimit(50)


class AVLTree(BinarySearchTree):

    # Override insert method from base class to keep it as AVL
    def insert(self, elem: object) -> None:
        """inserts a new node, with key and element elem"""
        self._root = self._insert(self._root, elem)

    def _insert(self, node: BinaryNode, elem: object) -> BinaryNode:
        """gets a node, searches the place to insert a new node with element e (using super()._insert),  and then,
        the function has to balance the node returned by the function super.()_insert"""
        node = super()._insert(node, elem)
        node = self._rebalance(node)
        return node

    # Override remove method from base class to keep it as AVL
    def remove(self, elem: object) -> None:
        self._root = self._remove(self._root, elem)

    def _remove(self, node: BinaryNode, elem: object) -> BinaryNode:
        """ gets a node, searches the node with element elem in the subtree that hangs down node , and
        then remove this node (using super()._remove). After this, the function has to balance the node returned by the function super()._remove"""
        node = super()._remove(node, elem)
        node = self._rebalance(node)
        return node

    def _rebalance(self, node: BinaryNode) -> BinaryNode:
        if self.isBalanced():
            return self._root



        return node

    def isBalanced(self):
        return self._isBalanced(self._root)

    def _isBalanced(self, node):
        if node:
            return abs(self._getBalanceFactor(node)) <= 1 and \
                   self._isBalanced(node.left) and \
                   self._isBalanced(node.right)
        else:
            return True

    def _getBalanceFactor(self, node):
        """Returns the number, signed"""
        if node is None:
            return 0
        else:
            return self._height(node.left) - self._height(node.left)

    def rightRotation(self, node: BinaryNode):
        # The node required is the root of the original structure
        new_root = node.left  # The new root of the subtree
        if node.right:
            new_root.right = node.right  # Selects the node that is going to change branches completely and moves it
        new_root.left = node  # Moves the previous root as the right son of the new root
        return new_root

    def leftRotation(self, node: BinaryNode):
        if not node.right:  # If it does not have a right node, do nothing
            return node
        new_root = node.right
        if new_root.left:
            node.right = node.right.left
        new_root.left = node
        return new_root
