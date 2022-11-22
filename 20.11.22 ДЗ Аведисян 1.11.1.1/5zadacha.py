#Сложность O(n)
class Solution():
    def getDescentPeriods(self, prices):
        n=len(prices)
        dp=[0]*n
        count=1
        for i in range(n):
            if i==0:
                dp[0]=1
                continue
            if prices[i-1]-prices[i]==1:
                dp[i]=dp[i-1]+1+count
                count+=1
            else:
                dp[i]=dp[i-1]+1
                count=1
        return dp[-1]


print(Solution.getDescentPeriods("",[3,2,1,4]))