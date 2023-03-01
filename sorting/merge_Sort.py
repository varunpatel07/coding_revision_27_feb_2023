class mergeSort:


    def merge(self,arr,low,mid,high):
        res=[]
        left=low
        right=mid+1
        while(left<=mid and right<=high):
            if(arr[left]<=arr[right]):
                res.append(arr[left])
                left+=1
            else:
                res.append(arr[right])
                right+=1  

        while(left<=mid):
            res.append(arr[left])
            left+=1

        while(right<=high):
            res.append(arr[right])
            right+=1

        for i in range(low,high+1):
            arr[i]=res[i-low]


    def sort(self,arr,low,high):
        if(low>=high):
            return
        mid=(low+high)//2
        #mid = low+((high-low)/2)
        self.sort(arr,low,mid)
        self.sort(arr,mid+1,high)
        self.merge(arr,low,mid,high)

        pass

obj=mergeSort()
arr = [45,3,2,-1,1,-43,5]
#arr=[1,2,3]
obj.sort(arr,0,len(arr)-1)
print(arr)