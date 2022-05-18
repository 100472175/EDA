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

    def right_rotate(self, node: BinaryNode) -> BinaryNode:
        """
        Perform a right rotation on the subtree rooted at node.
        :param node: the root node of the subtree to rotate
        :return: the new root of the rotated subtree
        """
        left_child = node.left
        node.left = left_child.right
        left_child.right = node
        return left_child

    def left_rotate(self, node: BinaryNode) -> BinaryNode:
        """
        Perform a left rotation on the subtree rooted at node.
        :param node: the root node of the subtree to rotate
        :return: the new root of the rotated subtree
        """
        right_child = node.right
        node.right = right_child.left
        right_child.left = node
        return right_child

    def RightLeftRotate(self, node: BinaryNode) -> BinaryNode:
        """
        Perform a right-left rotation on the subtree rooted at node.
        :param node: the root node of the subtree to rotate
        :return: the new root of the rotated subtree
        """
        node.right = self.right_rotate(node.right)
        return self.left_rotate(node)

    def LeftRightRotate(self, node: BinaryNode) -> BinaryNode:
        """
        Perform a left-right rotation on the subtree rooted at node.
        :param node: the root node of the subtree to rotate
        :return: the new root of the rotated subtree
        """
        node.left = self.left_rotate(node.left)
        return self.right_rotate(node)

    def _rebalance(self, node: BinaryNode) -> None:
        """
        Rebalance the subtree rooted at node.
        :param node: the root node of the subtree to rebalance
        :return: None
        """
        if node is None:
            return
        balance = self.get_balance(node)
        if balance > 1:
            if self.get_balance(node.left) < 0:
                node.left = self.left_rotate(node.left)
            node = self.right_rotate(node)
        elif balance < -1:
            if self.get_balance(node.right) > 0:
                node.right = self.right_rotate(node.right)
            node = self.left_rotate(node)
        self._rebalance(node.left)
        self._rebalance(node.right)


    def get_balance(self, node: BinaryNode) -> int:
        """
        Return the balance factor of the subtree rooted at node.
        :param node: the root node of the subtree
        :return: the balance factor of the subtree rooted at node
        """
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    # Override remove method from base class to keep it as AVL
    def remove(self, elem: object) -> None:
        self._root = self._remove(self._root, elem)

    def _remove(self, node: BinaryNode, elem: object) -> BinaryNode:
        ...
