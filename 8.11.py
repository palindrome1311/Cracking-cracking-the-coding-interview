def coinChange(n,denoms,dp,index):
    if(index>=len(denoms)-1):
        return 1
    if(dp[n][index]>0):
        return dp[n][index]
    i=0
    ways=0
    while(i * denoms[index] <= n):
        rem = (n - (i*denoms[index]))
        ways+= coinChange(rem,denoms,dp,index+1)
        i+=1
    dp[n][index] = ways
    return ways


n=11
denoms = [25,10,5,1]
dp=[[0]*len(denoms)]*(n+1)
print(coinChange(n,denoms,dp,0))