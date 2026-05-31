# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def helper(root):
            if not root:
                return 0
            
            left_height = helper(root.left)
            right_height = helper(root.right)

            if left_height == -1 or right_height == -1:
                return -1 
            if abs(left_height - right_height) > 1:
                return -1
            
            return 1 + max(left_height, right_height)

        return True if helper(root) != -1 else False
        