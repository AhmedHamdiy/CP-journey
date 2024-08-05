class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp =  [[[0 for i in range(3)] for j in range(3)] for k in range(n+1)]
        for i in range (n-1,-1,-1):
            for j in range (2):
                for k in range (2):
                    if j:
                        dp[i][j][k] = max(dp[i+1][1-j][k]-prices[i],dp[i+1][j][k])
                    else:
                        dp[i][j][k] = max(dp[i+1][1-j][k-1]+prices[i],dp[i+1][j][k])
        return dp[0][1][1]