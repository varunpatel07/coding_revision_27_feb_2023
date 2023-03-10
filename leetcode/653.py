# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        q=[root]
        cout=set()
        while(q):
            val = q.pop(0)
            if(val.val not in cout):
                cout.add(k - val.val)
                if(val.left):
                    q.append(val.left)
                if(val.right):
                    q.append(val.right)
            else:
                return True
        return False