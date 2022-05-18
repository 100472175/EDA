# from binarysearchtree import BinarySearchTree

from bst import BinarySearchTree
from bst import BinaryNode


class AVLTree(BinarySearchTree):

    def insert(self, data):
        self._root = self.insert_node(self._root, data)

    def insert_node(self, node, data):
        # super()._insert(node, data)
        # This is the same as the _insert function of bst.py, but for some reason, it does not work
        if node is None:
            return BinaryNode(data)

        if node.elem == data:
            print('Error: elem already exist ', data)
            return node

        if data < node.elem:
            node.left = self.insert_node(node.left, data)

        else:
            node.right = self.insert_node(node.right, data)

        return self.balance(node)

    def balance(self, root):
        if self.get_balance(root) > 1:
            if self.get_balance(root.left) < 0:
                root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if self.get_balance(root) < -1:
            if self.get_balance(root.right) > 0:
                root.right = self.rotate_right(root.right)
            return self.rotate_left(root)
        return root

    def height(self) -> int:
        """Returns the height of the tree"""
        return self.get_height(self._root)

    def get_height(self, node: BinaryNode) -> int:
        """return the height of node"""
        if node is None:
            return -1
        else:
            return 1 + max(self.get_height(node.left), self.get_height(node.right))

    def get_balance(self, root):
        if root is None:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def rotate_right(self, root):
        new_root = root.left
        root.left = new_root.right
        new_root.right = root
        return new_root

    def rotate_left(self, root):
        new_root = root.right
        root.right = new_root.left
        new_root.left = root
        return new_root

    def get_min(self, root):
        if root.left is None:
            return root
        return self.get_min(root.left)

    def get_max(self, root):
        if root.right is None:
            return root
        return self.get_max(root.right)


    def remove(self, data):
        self._root = self.delete_node(self._root, data)
        self._root = self.balance(self._root)

    def delete_node(self, root, data):
        if root is None:
            return root
        if data < root.elem:
            root.left = self.delete_node(root.left, data)
        elif data > root.elem:
            root.right = self.delete_node(root.right, data)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.get_min(root.right)
            root.elem = temp.elem
            root.right = self.delete_node(root.right, temp.elem)
        return self.balance(root)