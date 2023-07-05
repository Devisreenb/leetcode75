class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res=[]
        maxi = max(candies)
        for candy in candies:
            if candy+extraCandies >= maxi :
                res.append(True)
            else:
                res.append(False)
        return res

''' bruteforce 
        for i in range(len(candies)):
            candies[i]=candies[i]+extraCandies
            if candies[i] == max(candies) : 
                res.append(True)
            else:
                res.append(False)
            candies[i]=candies[i]-extraCandies
        return res

        '''
    
# TC - O(N)