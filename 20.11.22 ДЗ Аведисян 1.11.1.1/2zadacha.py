#Сложность O(n)
#Если наш индекс четный - мы делим индекс на 2 и добавляем этот результат к нашему массиву.
#Если наш индекс нечетный - мы делим индекс на 2
#Учитывая только его целое число, то есть делим нацело и используем этот индекс и следующий из этого индекса.
class Solution():
    def getMaximumGenerated(self,n):
        if n==0:
            return 0
        num=[0,1]
        for i in range(2,n+1):
            if i%2==0:
                num.append(num[i//2])
            else:
                num.append(num[i//2]+num[i//2 + 1])
        return max(num)


print(Solution.getMaximumGenerated("",7))