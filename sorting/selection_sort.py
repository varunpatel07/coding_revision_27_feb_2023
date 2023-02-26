#it is a modified version of bubble sort in which we select the minimum element and then swap it to correct postition
#complexity: O(N)

def sort(arr):
    n= len(arr)
    for i in range(n):
        minidx=i
        isChanged=False
        for j in range(i+1,n):
            if(arr[j]<arr[minidx]):
                isChanged=True
                minidx=j
        if(isChanged):
            arr[i],arr[minidx]=arr[minidx],arr[i]
        else:
            return



arr = [2,5,6,1,-5,9,-1,0]
#arr=[1,2,3]
sort(arr)
print(arr)

"""
a=3
b=5
a = 15
b= 3
a=5
"""