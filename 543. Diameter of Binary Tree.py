# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.cache = {}

        def depth(node):
            if not node:
                return 0
            
            key_left = (node.left,)
            key_right = (node.right,)

            if not self.cache.get(key_left):
                self.cache[key_left] = depth(node.left)
            if not self.cache.get(key_right):
                self.cache[key_right] = depth(node.right)

            left = self.cache.get(key_left)
            right = self.cache.get(key_right)

            self.diameter = max(self.diameter, left + right)

            return 1 + max(left, right)

        depth(root)
        return self.diameter