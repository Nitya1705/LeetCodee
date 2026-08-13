class Solution:
    def minDepth(self, root):
        if root is None:
            return 0

        # If left child is missing, go through right subtree
        if root.left is None:
            return 1 + self.minDepth(root.right)

        # If right child is missing, go through left subtree
        if root.right is None:
            return 1 + self.minDepth(root.left)

        # Both children exist
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))