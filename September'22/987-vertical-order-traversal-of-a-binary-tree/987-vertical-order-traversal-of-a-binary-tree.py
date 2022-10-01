# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root, h_dist, v_dist, values):
            if not root:
                return
            
            if v_dist in values:
                values[v_dist].append((h_dist, root.val))
            else:
                values[v_dist] = [(h_dist, root.val)]
                
            self.verticalOrder(root.left, h_dist + 1, v_dist - 1, values)
            self.verticalOrder(root.right, h_dist + 1, v_dist + 1, values)
            
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        v_dist = 0
        h_dist = 0
        values = {}  
        result = []
        
        self.verticalOrder(root, h_dist, v_dist, values)
        
        for x in sorted(values.keys()):
            column = [i[1] for i in sorted(values[x])]
            result.append(column)

        return result
        