class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        a={}
        b=[]
        for x in nums:
            if x in a:
                a[x]+=1
            else:
                a[x]=1
            if a[x]>=k:
                b.append(x)
        return list(set(b))
        
        
        
            
        