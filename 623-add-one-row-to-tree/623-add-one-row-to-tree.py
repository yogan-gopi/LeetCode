# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def helper(node, val, depth, curDepth):
            if not node:
                return
            if curDepth == depth-1:
                temp = node.left
                node.left = TreeNode(val)
                node.left.left = temp
                
                temp = node.right
                node.right = TreeNode(val)
                node.right.right = temp
            else:
                helper(node.left, val, depth, curDepth+1)
                helper(node.right, val, depth, curDepth+1)
                
                
        if depth == 1:
            node = TreeNode(val)
            node.left = root
            return node
        
        helper(root, val, depth, 1)
        return root        
        
        
        