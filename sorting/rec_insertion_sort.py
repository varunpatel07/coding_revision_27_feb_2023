def insertion_sort(arr,idx):

    key = arr[idx]
    j=idx-1
    while(j>=0 and arr[j]>key):
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]= key
    
    pass


arr = [45,3,2,-1,1,-43,5]
arr=[4,2,1,3] #2413 1243
n=1
insertion_sort(arr,n)
print(arr)