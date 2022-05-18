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

    def old_rebalance(self, node: BinaryNode) -> BinaryNode:
        """ gets node and balances it"""
        """bf_node = self.getBalanceFactor(node)
        if abs(bf_node) <= 1:
            self.getBalanceFactor(node.left)
            self.getBalanceFactor(node.right)

        while self.getBalanceFactor(node) > 1:
            self.rightRotation(node)

        while self.getBalanceFactor(node) < 1:
            self.leftRotation(node)"""

        while abs(self.getBalanceFactor(node)) > 1:
            if self.getBalanceFactor(node) >= 2 and self.getBalanceFactor(node.left) == 1:
                self.rightRotation(node)

            if self.getBalanceFactor(node) >= 2 and self.getBalanceFactor(node.left) == -1:
                self.leftRightRotation(node)

            if self.getBalanceFactor(node) <= -2 and self.getBalanceFactor(node.right) == -1:
                self.leftRotation(node)

            if self.getBalanceFactor(node) <= -2 and self.getBalanceFactor(node.right) == 1:
                self.rightLeftRotation(node)
        if node.left is not None:
            if self.getBalanceFactor(node.left) != 0:
                self._rebalance(node.left)
        if node.right is not None:
            if self.getBalanceFactor(node.right) != 0:
                self._rebalance(node.right)

        return node

    def _rebalance(self, node: BinaryNode) -> BinaryNode:
        if self.isBalanced():
            return self._root


        return node

    def isBalanced(self):
        node = self._root
        return self._isBalanced(node)

    def _isBalanced(self, node):
        if abs(self._getBalanceFactor(node)) > 1:
            return False
        else:
            return self._getBalanceFactor(node) <= 1 and \
                    self._getBalanceFactor(node.right) and \
                    self._getBalanceFactor(node.left)

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

    def leftRotation(self, node: BinaryNode):
        if not node.right:  # If it does not have a right node, do nothing
            return node
        new_root = node.right
        if new_root.left:
            node.right = node.right.left
        new_root.left = node
        return node.right

    def rightRotation(self, node: BinaryNode):
        if not node.left:  # If it does not have a right node, do nothing
            return node
        new_root = node.left
        if new_root.right:
            node.left = node.left.right
        new_root.right = node
        return new_root





"""
old code:
    def leftRotation(self, node: BinaryNode):
        # The node required is the root of the original structure
        new_root = node.right
        if node.left is not None:
            new_root.left = node.left
        new_root.right = node
        if node.parent is not None:
            new_root.parent = node.parent
            node.parent.left = new_root
        node.parent = new_root
        return new_roort

    def rightRotation(self, node: BinaryNode):
        # The node required is the root of the original structure
        new_root = node.left  # The new root of the subtree
        if node.right is not None:
            new_root.right = node.right  # Selects the node that is going to change branches completely and moves it
        new_root.left = node  # Moves the previous root as the right son of the new root
        if node.parent is not None:
            new_root.parent = node.parent
            node.parent.right = new_root
        node.parent = new_root  # 
        return new_root

    def leftRightRotation(self, node: BinaryNode):
        # The node required is the root of the original strucuture
        self.leftRotation(node.left)
        self.rightRotation(node)

    def rightLeftRotation(self, node: BinaryNode):
        # The node required is the root of the original BSTtree
        self.rightRotation(node.right)
        self.leftRotation(node)

    def getBalanceFactor(self, node):
        if node is not None:
            if node.right is not None:
                r = self._height(node.right)
            else:
                r = 0
            if node.left is not None:
                l = self._height(node.left)
            else:
                l = 0

            return r-l
        else:
            return 0
"""


