class Solution:
    def firstUniqChar(self, s: str) -> int:
        store={}
        for i in range(len(s)):
            if(s[i] not in store):
                store[s[i]]=[0,i]
            store[s[i]][0]+=1
        
        for idx,val in store.items():
            if(val[0]==1):
                return val[1]
        return -1


