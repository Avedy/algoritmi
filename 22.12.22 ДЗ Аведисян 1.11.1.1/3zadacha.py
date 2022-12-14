#Сложность O(n)
class Solution:
    def tribonacci(self, n):
        if n <= 2:
            if n == 0:
                return 0
            if n == 1 or n == 2:
                return 1
        else:
            arr = [1] * (n + 1)
            arr[0] = 0
            arr[2] = 1
            for i in range(3, n + 1):
                arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3]
        return arr[n]