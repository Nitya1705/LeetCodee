class Solution:
    def reverseOddLevels(self, root):
        def dfs(left, right, level):
            if not left or not right:
                return

            # Odd level: swap the values
            if level % 2 == 1:
                left.val, right.val = right.val, left.val

            dfs(left.left, right.right, level + 1)
            dfs(left.right, right.left, level + 1)

        dfs(root.left, root.right, 1)
        return root