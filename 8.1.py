def util(dp,n):
        if dp[n]!=-1:
            return dp[n]
        else:
            dp[n] = util(dp,n-1) + util(dp,n-2), util(dp,n-3)
            return dp[n]
class Solution:
    def climbStairs(self, n: int) -> int:
        if(n==1):
            return 1
        if(n==2):
            return 2
        dp=[-1]*(n+1)
        dp[1]=1
        dp[2]=2
        return util(dp,n)