from bst import BinarySearchTree


class BinaryExercises(BinarySearchTree):
    def _maximum_rec(self, node):
        if node is None:
            return None
        if node.right is None:
            return node.elem
        return self._maximum_rec(node.right)


    def minimum(self):
        return self._minimum(self._root)

    def _minimum(self, node):
        if node is None:
            return None
        while node.left:
            node = node.left
        return node.elem

    def _predecesor(self, node):
        if node is None:
            return None
        if not node.left:
            return None
        node = node.left
        while node.right:
            node = node.right
        return node.elem

    def _succesor(self, node):
        if node is None:
            return None
        if not node.right:
            return None
        node = node.right
        while node.left:
            node = node.left
        return node.elem