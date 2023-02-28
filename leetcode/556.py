class Solution:
    def matrixReshape(self, mat, r, c):

        result=[[0]*c for _ in range(r)]
        print

        curr_row=0
        curr_col=0


        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if(curr_col<c):
                    result[curr_row][curr_col]=mat[i][j]
                    curr_col+=1

                else:
                    curr_row+=1
                    curr_col=0
                    result[curr_row][curr_col]=mat[i][j]
                    curr_col+=1


        return result


        

        print(result)

obj= Solution()
mat = [[1,2],[3,4]]
r = 1
c = 4
print(obj.matrixReshape(mat,r,c))
