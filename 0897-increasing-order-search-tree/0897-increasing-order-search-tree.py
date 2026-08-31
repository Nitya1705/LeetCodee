class Solution:
    def increasingBST(self, root):
        dummy = TreeNode(0)
        current = dummy

        def inorder(node):
            nonlocal current

            if node is None:
                return

            inorder(node.left)

            node.left = None
            current.right = node
            current = node

            inorder(node.right)

        inorder(root)

        return dummy.right
         