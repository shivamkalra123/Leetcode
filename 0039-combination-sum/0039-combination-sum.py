class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        subset=[]
        def dfs(i,curr_sum):
            if i>=len(candidates) or curr_sum>target:
                return
            if curr_sum==target:
                result.append(subset.copy())
                return
            
            subset.append(candidates[i])
            dfs(i,curr_sum+candidates[i])

            subset.pop()
            dfs(i+1,curr_sum)
        dfs(0,0)
        return result

        