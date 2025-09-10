class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c=0
        a = {0: 1} 
        count=0
        for j in nums:
            c+=j
            if c-k in a:
                count+=a[c-k]
            if c in a:
                a[c]+=1
            else:
                a[c]=1
        return count

        
