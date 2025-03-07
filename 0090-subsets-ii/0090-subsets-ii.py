class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result=set()
        subset=[]
        def dfs(i):
            if i>len(nums):
                return
            if i==len(nums):
                result.add(tuple(subset))
                return
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        nums.sort()
        dfs(0)
        return [list(s) for s in result]
        
            



