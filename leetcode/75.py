class Solution:
    def sortColors1(self, nums):
        low=0
        curr=0
        high=len(nums)-1
        while(curr<=high):
            if(nums[curr]==0):
                nums[low],nums[curr]=nums[curr],nums[low]
                low+=1
                curr+=1
            elif(nums[curr]==1):
                curr+=1
            elif(nums[curr]==2):
                nums[high],nums[curr]=nums[curr],nums[high]
                high-=1


        pass


obj= Solution()
arr=[2,0,2,1,1,0]
arr2=[1,2,0]
obj.sortColors1(arr)
print(arr)
