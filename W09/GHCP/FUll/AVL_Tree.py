# Import queue and stack


class Node:
    def __init__(self, data):
        self.elem = data
        self.left = None
        self.right = None
        self.height = 1

    def __eq__(self, other: 'Node') -> bool:
        """checks if two nodes (subtrees) are equal o not"""
        return other is not None and self.elem == other.elem and self.left == other.left and self.right == other.right

    def __str__(self):
        return str(self.elem)


class AVLTree(object):
    def __init__(self, root=None):
        self._root = root
        self.size = self.get_size(root)

    def get_size(self, root):
        if root is None:
            return 0
        return 1 + self.get_size(root.left) + self.get_size(root.right)

    def insert(self, data):
        self._root = self.insert_node(self._root, data)

    def insert_node(self, root, data):
        if root is None:
            return Node(data)
        if data < root.elem:
            root.left = self.insert_node(root.left, data)
        else:
            root.right = self.insert_node(root.right, data)
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        return self.balance(root)

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

    def get_height(self, root) -> int:
        if root is None:
            return 0
        return root.height

    def get_balance(self, root):
        if root is None:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def rotate_right(self, root):
        new_root = root.left
        root.left = new_root.right
        new_root.right = root
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))
        return new_root

    def rotate_left(self, root):
        new_root = root.right
        root.right = new_root.left
        new_root.left = root
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))
        return new_root

    def remove(self, data):
        self._root = self.delete_node(self._root, data)

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
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        return self.balance(root)

    def get_min(self, root):
        if root.left is None:
            return root
        return self.get_min(root.left)

    def get_max(self, root):
        if root.right is None:
            return root
        return self.get_max(root.right)

########################################################################################################################

    """def inorder(self):
        self.inorder_node(self._root)

    def inorder_node(self, root):
        if root is None:
            return
        self.inorder_node(root.left)
        print(root.elem)
        self.inorder_node(root.right)

    def preorder(self):
        self.preorder_node(self._root)

    def preorder_node(self, root):
        if root is None:
            return
        print(root.elem)
        self.preorder_node(root.left)
        self.preorder_node(root.right)

    def postorder(self):
        self.postorder_node(self._root)

    def postorder_node(self, root):
        if root is None:
            return
        self.postorder_node(root.left)
        self.postorder_node(root.right)
        print(root.elem)

    def search(self, data):
        return self.search_node(self._root, data)

    def search_node(self, root, data):
        if root is None:
            return None
        if data < root.elem:
            return self.search_node(root.left, data)
        elif data > root.elem:
            return self.search_node(root.right, data)
        return root"""

    def draw(self) -> None:
        """function to draw a tree. """
        if self._root:
            self._draw('', self._root, False)
        else:
            print('tree is empty')
        print('\n\n')

    def _draw(self, prefix: str, node: Node, is_left: bool) -> None:
        if node is not None:
            self._draw(prefix + "     ", node.right, False)
            print(prefix + "|-- " + str(node.elem))
            self._draw(prefix + "     ", node.left, True)
