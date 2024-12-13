class Solution:
    def climbStairs(self, n: int) -> int:
        dp={}
        def solve(N):
            if N==0:
                return 1
            if N<0:
                return 0
            if N in dp:
                return dp[N] 
            dp[n]=solve(N-1)+solve(N-2)
            return dp[n]
        return solve(n)

        
        
        