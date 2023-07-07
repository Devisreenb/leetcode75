class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        
        n = len(nums)-1
        i=0
        count=0
        while n>=0:
            if nums[i]==0:
                nums.pop(i)
                count+=1
                n-=1
            else:
                i+=1
                n-=1
        for i in range(count):
            nums.append(0)
        

