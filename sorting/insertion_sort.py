#we have 2 part in this array one is sorted another is unsorted we pick an element and backtrack it until we find
# its correct position
#O(N2)
def sort(arr):


    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while(j>=0 and arr[j]>key):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key

    pass

arr = [2,5,6,1,-5,9,-1,0]
#arr=[1,2,3]
sort(arr)
print(arr)