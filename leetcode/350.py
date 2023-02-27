class Solution:
    def intersect(self, nums1, nums2):
        #intition is that we would store count of bount list in 

        store_1 = {}
        store_2 = {}

        res=[]
        for num in nums1:
            if(num not in store_1):
                store_1[num]=0
            store_1[num]+=1


        for num in nums2:
            if(num not in store_2):
                store_2[num]=0
            store_2[num]+=1

        for key,val in store_1.items():
            if(key in store_2):
                res.extend([key]*min(store_1[key],store_2[key]))
        return res
    
obj=Solution()
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

print(obj.intersect(nums1,nums2))