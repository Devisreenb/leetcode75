#BruteForce 
class Solution:
    def reverseVowels(self, s: str) -> str:
        v=[]
        for i in s:
            if i.lower() in ('a','e','i','o','u'):
                v.append(i)
        ls = [i for i in s]
        for i in range(len(s)):
            if ls[i].lower() in ("a",'e','i','o','u'):
                ls[i] = v.pop()
        res = "".join(ls)
        return res


# Optimal Solution - Two pointer Approach - TC : O(N/2)
class Solution:
    def reverseVowels(self, s: str) -> str:
        l = 0
        r = len(s)-1
        vowels = ('a','e','i','o','u','A','E','I','O','U')
        ls = list(s)
        while l<r:
            if ls[l] in vowels and ls[r] in vowels :
                ls[l],ls[r] = ls[r],ls[l]
                l+=1
                r-=1
            elif ls[l] not in vowels :
                l+=1
            elif ls[r] not in vowels:
                r-=1
        return "".join(ls)

