#bruteforce
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        t1 = len(word1)
        t2 = len(word2)
        new = ""
        if t2>t1:
            r = t1
        else:
            r = t2
        for i in range(r):
            new+=word1[i]+word2[i]
        if t1>t2:
            new+=word1[i+1:]
        else:
            new+=word2[i+1:]
        return new

'''
# Optimal - This is two pointer approach

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        t1 = len(word1)
        t2 = len(word2)
        i = 0
        j = 0
        new = ""
        while(i<t1 or i<t2):
            if (i<t1):
                new+=word1[i]
                
            if(j<t2):
                new+=word2[j]
                
            i+=1
            j+=1
        return new
'''