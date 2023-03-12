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


obj= Solution()
arr=[0,1,1,0]
arr2=[1,0,0,1,1]
obj.sortColors1(arr)
print(arr)
