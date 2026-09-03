# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []

        # Inorder traversal
        def inorder(node):
            if node is None:
                return

            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)

        # Build balanced BST
        def build(low, high):
            if low > high:
                return None

            mid = (low + high) // 2

            node = TreeNode(arr[mid])

            node.left = build(low, mid - 1)
            node.right = build(mid + 1, high)

            return node

        inorder(root)

        return build(0, len(arr) - 1)