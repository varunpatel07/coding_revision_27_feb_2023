class Solution:
    def searchMatrix(self, matrix, target):
        row=0
        col=len(matrix[0])-1
        while(row<len(matrix) and col>=0):
            if(matrix[row][col]==target):
                return True
            if(matrix[row][col]<target):
                row+=1
            else:
                col-=1
        return False

        
        pass

obj = Solution()
matrix = [[1,3,5,7],
          [10,11,16,20],
          [23,30,34,60]]
target = 27
print(obj.searchMatrix(matrix,target))