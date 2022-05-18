class AVLTree(object):
    """ AVL Tree """

    def __init__(self):
        """ Create an empty AVL Tree """
        self.root = None

    def add(self, val):
        """ Add a new item to the tree """
        # Check if tree is empty
        if self.root is None:
            self.root = AVLNode(val)
        else:
            self._add(self.root, val)

    def _add(self, curr_node, val):
        """ Add a new item to the tree """
        if val < curr_node.val:
            if curr_node.left is None:
                curr_node.left = AVLNode(val)
            else:
                self._add(curr_node.left, val)
        else:

            if curr_node.right is None:
                curr_node.right = AVLNode(val)
            else:
                self._add(curr_node.right, val)
        curr_node.height = 1 + max(self.get_height(curr_node.left), self.get_height(curr_node.right))
        self.balance(curr_node)

    def balance(self, curr_node):
        """ Balance the tree """
        if self.get_balance(curr_node) == 2:
            if self.get_balance(curr_node.left) == 1:
                self.rotate_left(curr_node.left)
            self.rotate_right(curr_node)
        elif self.get_balance(curr_node) == -2:
            if self.get_balance(curr_node.right) == -1:
                self.rotate_right(curr_node.right)
            self.rotate_left(curr_node)