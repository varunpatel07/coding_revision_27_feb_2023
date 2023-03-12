class Solution:
    def threeSum(self, nums):
        res=[]
        #nums=list(set(nums))
        nums.sort()
        for i,val in enumerate(nums):
            if(i!=0 and val==nums[i-1]):
                continue
            left,right=i+1,len(nums)-1
            while(left<right):
                if(nums[i]+nums[left]+nums[right]==0):
                    res.append([nums[i],nums[left],nums[right]])
                    left+=1
                    while(nums[left]==nums[left-1] and left<right):
                        left+=1
                else:
                    if(nums[i]+nums[left]+nums[right]>0):
                        right-=1
                    else:
                        left+=1
        return res


        pass



obj= Solution()
nums = [-1,0,1,2,-1,-4]
print(obj.threeSum(nums))
# -4,-1,0,1,2
