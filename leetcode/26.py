class Solution:
    def removeDuplicates(self, nums):

        k = 1
        i = 0
        for i in range(1,len(nums)):
            if(nums[k-1]!=nums[i]):
                nums[k] = nums[i]
                k+=1
        return k

obj = Solution()
nums = [0,0,1,1,1,2,2,3,3,4] #5
#obj.removeDuplicates(nums)
print(obj.removeDuplicates(nums))
#print(nums)
nums = [1,1,2] #2
print(obj.removeDuplicates(nums))
nums = [1,2,3] #3
print(obj.removeDuplicates(nums))
