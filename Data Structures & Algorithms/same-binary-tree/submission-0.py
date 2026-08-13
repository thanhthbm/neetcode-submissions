# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p_root: Optional[TreeNode], q_root: Optional[TreeNode]) -> bool:
            if not p_root and not q_root:
                return True
            if not p_root and q_root:
                return False
            if not q_root and p_root:
                return False
            if q_root.val != p_root.val:
                return False
            
            return dfs(q_root.left, p_root.left) and dfs(q_root.right, p_root.right)

        return dfs(p, q)