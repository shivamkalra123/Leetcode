class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def back(st, res):
            if st == len(nums):
                return res == target
            return back(st + 1, res + nums[st]) + back(st + 1, res - nums[st])

        return back(0, 0)
            