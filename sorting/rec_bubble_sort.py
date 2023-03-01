def rec_bubble_sort(arr,n):
    if(n==1):
        return 
    
    for i in range(n-1):
        if(arr[i]>arr[i+1]):
            arr[i],arr[i+1]=arr[i+1],arr[i]
    
    rec_bubble_sort(arr,n-1)



    pass



#obj=mergeSort()
arr = [45,3,2,-1,1,-43,5]
#arr=[1,2,3]
n=len(arr)
rec_bubble_sort(arr,n)
print(arr)