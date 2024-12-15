class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[]
        for i in range(n+1):
            a=bin(i)
            b=a.count("1")
            ans.append(b)
            # ans.append(a.count(1))
        return ans
        