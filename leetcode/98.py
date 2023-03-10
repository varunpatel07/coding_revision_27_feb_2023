# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if(root==None or (root.left==None and root.right==None)):
            return True
        def helper(root,arr):
            if(root==None):
                return
            if(root.left):
                helper(root.left,arr)
            arr.append(root.val)
            if(root.right):
                helper(root.right,arr)
            return arr
        arr=helper(root,[])
        for i in range(1,len(arr)):
            if(arr[i-1]>=arr[i]):
                return False
        return True



#########2############

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root,minv=-sys.maxsize,maxv=sys.maxsize):
            if(root==None):
                return True
            return root.val>minv and root.val<maxv and helper(root.left,minv,root.val) and helper(root.right,root.val,maxv)
        
        return helper(root)
        