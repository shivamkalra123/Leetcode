class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        res=[[] for i in range(len(nums)+1)]
        for j in nums:
            hashmap[j]=1+hashmap.get(j,0)
        for i,e in hashmap.items():
            res[e].append(i)
        output=[]
        for i in range(len(res)-1,0,-1):
            for num in res[i]:
                output.append(num)
                if len(output)==k:
                    return output


        