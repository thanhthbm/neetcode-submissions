# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def pathSum(root: Optional[TreeNode], target) -> bool:
            if not root:
                return False

            target -= root.val
            if not root.left and not root.right:
                return target == 0

            left = pathSum(root.left, target)
            right = pathSum(root.right, target)
            return pathSum(root.left, target) or pathSum(root.right, target)
        return pathSum(root, targetSum)
