class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        f=s = float('inf')

        for i in range(len(nums)):
            if nums[i]<=f:
                f = nums[i]
            elif nums[i]<=s:
                s = nums[i]
            elif nums[i]>s:
                return True
        return False



        '''
        prefix_min = []
        for i in range(len(nums)):
            prefix_min.append(min(nums[:i+1]))
        postfix_max = []
        for i in range(len(nums)-1,-1,-1):
            postfix_max.append(max(nums[i:]))
        postfix_max.reverse()
        for i in range(len(nums)):
            if prefix_min[i]<nums[i] and nums[i]<postfix_max[i]:
                return True
        return False
        '''

        
        '''
        for i in range(len(nums)) :
             for j in range(i,len(nums)):
                 for k in range(j,len(nums)):
                     if i<j<k and nums[i]<nums[j]<nums[k]:
                         return True
        return False
        '''