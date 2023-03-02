"""
if length is not same then return false
if number of non duplicate element is not same then return False
then compare elements in both string 
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        if(len(set(s))!=len(set(t))):
            return False
        store={}

        for word in s:
            if(word not in store):
                store[word]=0
            store[word]+=1

        for word in t:
            if(word not in store or store[word]<=0):
                return False
            store[word]-=1 
        return True