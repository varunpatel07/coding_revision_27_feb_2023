class Solution:
    def canConstruct(self, ransomNote, magazine):
        #samast ka dimaag
        store={}

        for word in magazine:
            if(word not in store):
                store[word]=0
            store[word]+=1

        for word in ransomNote:
            if(word not in store or store[word]<=0):
                return False
            store[word]-=1 
        return True


ransomNote = "aaa"
magazine = "aab"
obj=Solution()


