"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res: list[int] = []

        def postorder(root: 'Node') -> None:
            if not root:
                return
            
            if root.children:
                for child in root.children:
                    postorder(child)

            res.append(root.val)

        postorder(root)
        return res