from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        current_left_sum = 0
        count = 0


        for i in range(len(nums) - 1):  
            current_left_sum += nums[i]  
            right_sum = total_sum - current_left_sum 

            if current_left_sum >= right_sum:
                count += 1

        return count
