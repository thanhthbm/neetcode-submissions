# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p or not q: 
                return p is q
            if p.val != q.val:
                return False

            return (sameTree(q.left, p.left) and sameTree(q.right, p.right))

        def dfs(root: Optional[TreeNode]) -> bool:
            if not root:
                return False
            
            if sameTree(root, subRoot):
                return True

            return dfs(root.left) or dfs(root.right)

        return dfs(root) 