# from binarysearchtree import BinarySearchTree
from bst import BinarySearchTree
from bst import BinaryNode


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

    def leftRotation(self, node: BinaryNode):
        """The node required is the root of the original BSTtree"""
        new_root = node.right
        if node.right.left is not None:
            node.right = node.right.left
        new_root.right = node
        if node.parent is not None:
            new_root.parent = node.parent
            node.parent.left = new_root
        node.parent = new_root

    def rightRotation(self, node: BinaryNode):
        """The node required is the root of the original BSTtree"""
        new_root = node.left  # The new root of the subtree
        if node.left.right is not None:
            node.left = node.left.right  # Selects the node that is going to change branches completely and moves it
        new_root.right = node  # Moves the previous root as the right son of the new root
        if node.parent is not None:
            new_root.parent = node.parent
            node.parent.right = new_root
        node.parent = new_root  #

    def leftRightRotation(self, node: BinaryNode):
        """The node required is the root of the original BSTtree"""
        self.leftRotation(node.left)
        self.rightRotation(node)

    def rightLeftRotation(self, node: BinaryNode):
        """The node required is the root of the original BSTtree"""
        self.rightRotation(node.right)
        self.leftRotation(node)

    def getBalanceFactor(self, node):
        return self._height(node.right) - self._height(node.left)

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
        """ gets node and balances it"""
        """bf_node = self.getBalanceFactor(node)
        if abs(bf_node) <= 1:
            self.getBalanceFactor(node.left)
            self.getBalanceFactor(node.right)

        while self.getBalanceFactor(node) > 1:
            self.rightRotation(node)

        while self.getBalanceFactor(node) < 1:
            self.leftRotation(node)"""

        # Creo que habría que cambiar estos whiles por un while, o meterlos en un while gigante
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
            self._rebalance(node.left)
        if node.right is not None:
            self._rebalance(node.right)


        return node
