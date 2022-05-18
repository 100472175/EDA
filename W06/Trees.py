import queue


class SNode:
    def __init__(self, element, left=None, right=None, parent=None):
        self.parent = parent
        self.left = left
        self.right = right
        self.elem = element


class BinaryTree:
    def __init__(self):
        # Creates an empty binary tree
        self._root = None

    def size(self):
        """Returns the number of nodes in the tree"""
        return self._size(self._root)

    def _size(self, node):
        """Returns the size of the subtree from a specific node"""
        if node is None:
            return 0
        return 1 + self._size(node.left) + self._size(node.right)

    def height(self):
        return self._height(self._root)

    def _height(self, node):
        if node is None:
            return -1
        return 1 + max(self._height(node.left), self._height(node.right))

    def depth(self, node):
        """No me ha dado tiempo"""

    def preorder(self):
        self._preorder(self._root)

    def _preorder(self, node):
        if node is not None:
            print(node.elem)
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self):
        self._postorder(self._root)

    def _postorder(self, node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.elem)

    def inorder(self):
        self._inorder(self._root)

    def _inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.elem)
            self.inorder(node.right)

    def levelOrder(self):
        self._levelOrder(self._root)

    def _levelOrder(self, node):
        if self._root is None:
            print('tree is empty')
        else:

            q = queue.Queue()
            q.put(self._root)  # enqueue: we save the root

            while not q.empty():
                current = q.get()  # dequeue
                print(current.elem)
                if current.left is not None:
                    q.put(current.left)
                if current.right is not None:
                    q.put(current.right)


class BinarySearchTree(BinaryTree):
    """WIll be used in the future, but the importat part is that it inherits the class BinaryTree"""
