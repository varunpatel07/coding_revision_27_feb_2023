
class Solution:
    def generate(self, numRows):
        res=[]
        for i in range(numRows):
            inter = [0]*(i+1)
            inter[0]=1
            inter[-1]=1
            if(len(res)>0):
                for j in range(1,i):
                    inter[j]=res[i-1][j]+res[i-1][j-1]
            res.append(inter)
        return res

            

numRows = 5
obj= Solution()

print(obj.generate(numRows))
