def sort_1(arr):

    for i in range(len(arr)):
        s=1
        for j in range(i+1,len(arr)):
            if(arr[i]>arr[j]):
                s=0
                arr[i],arr[j]=arr[j],arr[i]
        #print(arr)
        if(s):
            return
#we continously check arr[i] and arr[i+1] and swap them    
# time complexity O(N2)        
def sort_2(arr):
    n=len(arr)
    for i in range(n):
        isswapped=False
        for j in range(n-i-1):
            if(arr[j]>arr[j+1]):
                isswapped=True
                arr[j],arr[j+1]=arr[j+1],arr[j]
        if(not isswapped):
            return
        




arr = [2,5,6,1,-5,9,-1,0]
#arr=[1,2,3]
sort_2(arr)
print(arr)
