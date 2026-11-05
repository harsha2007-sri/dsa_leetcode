# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        temp=root
        if root is None:
            nn=TreeNode(val)
            root=nn
            return root
        while root:
            p=root
            if val>root.val:
                root=root.right
            else:
                root=root.left
        nn=TreeNode(val)
        if val>p.val:
            p.right=nn
        else:
            p.left=nn
        return temp
        

