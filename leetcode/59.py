class Solution:
    def generateMatrix(self, n):
        top = 0
        left = 0
        bottom = n-1
        right = n-1
        res = [[0]*n for _ in range(n)]
        val = 1
        while(top<=bottom):
            for col in range(top,right+1):
                res[top][col] = val
                val+=1
            top+=1

            for row in range(top,bottom+1):
                res[row][right] = val
                val+=1

            right-=1

            for col in range(right,left-1,-1):
                res[bottom][col] = val
                val+=1
            
            bottom-=1

            for row in range(bottom,top-1,-1):
                res[row][left] = val
                val+=1
            left+=1

        return res
    
obj = Solution()

for row in obj.generateMatrix(3):
    print(row)




