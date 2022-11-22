#Сложность O(n)
class Solution():
    def maxProfit(self, prices):
        if not prices:
            return 0
        proffit=0
        for i, val in enumerate(prices):
            if i==0:
                continue
            if prices[i-1]<val:
                proffit+=val-prices[i-1]

        return proffit


print(Solution.maxProfit("",[7,1,5,3,6,4]))