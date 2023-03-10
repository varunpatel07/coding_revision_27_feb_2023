# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(root==None):
            return []
        res=[]
        q=[root,None]
        temp=[]
        while(q):
            curr=q.pop(0)
            if(curr!=None):
                temp.append(curr.val)
                if(curr.left):
                    q.append(curr.left)
                
                if(curr.right):
                    q.append(curr.right)
            else:
                if(len(q)!=0):
                    q.append(None)
                res.append(temp)
                temp=[]
                

                

        return res
