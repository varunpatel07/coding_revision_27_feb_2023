class Solution:
    def merge(self, nums1, m, nums2, n):
        # if(n==0):
        #     nums1=nums2
        if(n!=0):
            end_1=m-1
            end_2=n-1
            ptr = len(nums1)-1
            while(end_1>=0 and end_2>=0):
                if(nums1[end_1]>nums2[end_2]):
                    nums1[ptr]=nums1[end_1]
                    end_1-=1
                else:
                    nums1[ptr]=nums2[end_2]
                    end_2-=1
                ptr-=1

            if(end_2>=0):
                for i in range(end_2,-1,-1):
                    nums1[ptr]=nums2[i]
                    #end_2-=1
                    ptr-=1




obj = Solution()
nums1 = [8,0,0]
m = 1
nums2 = [-1,2]
n = 2
obj.merge(nums1,m,nums2,n)
print(nums1)