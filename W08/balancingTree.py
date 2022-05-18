from bintree import BinaryTree
from bintree import BinaryNode


class AVLTree(BinaryTree):

    def left_rotation(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        return y

    def right_rotation(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        return y

    def getHeight(self, root):
        # Check if the binary tree is empty
        if root is None:
            # If TRUE return 0
            return 0
            # Recursively call height of each node
        leftAns = self.getHeight(root.left)
        rightAns = self.getHeight(root.right)

        # Return max(leftHeight, rightHeight) at each iteration
        return max(leftAns, rightAns) + 1

    def getBalanceFactor(self, node):
        return self.getHeight(node.left) - self.getHeight(node.right)

    def insert(self, root, value):

        # Step 1 - Perform normal BST
        if not root:
            return BinaryNode(value)
        elif value < root.elem:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        # Step 2 - Get the balance factor
        balance = self.getHeight(root)

        # Step 3 - If the node is unbalanced, then try out the 4 different options:
        # Case 1 - Left Left
        if balance > 1 and value < root.left.elem:
            return self.right_rotation(root)

        # Case 2 - Right Right
        if balance < -1 and value > root.right.elem:
            return self.left_rotation(root)

        # Case 3 - Left Right
        if balance > 1 and value > root.left.elem:
            root.left = self.left_rotation(root.left)
            return self.right_rotation(root)

        # Case 4 - Right Left
        if balance < -1 and value < root.right.elem:
            root.right = self.right_rotation(root.right)
            return self.left_rotation(root)

        return root

tree = AVLTree()
tree.insert(tree._root, 5)
tree.preorder()