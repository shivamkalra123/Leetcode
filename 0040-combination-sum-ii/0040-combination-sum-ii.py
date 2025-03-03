from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # Sort to handle duplicates
        result = []
        subset = []

        def dfs(i, curr_sum):
            if curr_sum == target:
                result.append(subset.copy()) 
                return
            if i >= len(candidates) or curr_sum > target:
                return

            
            subset.append(candidates[i])
            dfs(i + 1, curr_sum + candidates[i])
            subset.pop()

            
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, curr_sum)  t

        dfs(0, 0)
        return result
