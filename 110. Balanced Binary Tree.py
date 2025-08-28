# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def inner(root):
            if root:
                left_height, left_balanced = inner(root.left)
                right_height, right_balanced = inner(root.right)

                balanced = (
                    left_balanced and
                    right_balanced and
                    abs(left_height - right_height) <= 1 
                )

                height = 1 + max(left_height, right_height)

                return height, balanced
            return 0, True

        return inner(root)[1]