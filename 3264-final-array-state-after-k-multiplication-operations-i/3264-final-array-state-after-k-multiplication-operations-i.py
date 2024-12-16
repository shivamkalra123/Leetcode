class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        def minNums(arr):
            return nums.index(min(nums))
        while k>0:
            a=minNums(nums)
            nums[a]*=multiplier
            k-=1
        return nums
            
        

        


