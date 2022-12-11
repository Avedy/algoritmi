#Сложность O(n)
class Solution(object):
    def getDecimalValue(self, head):
        string="" #создаем строку для значений.
        while head!=None: #проверяем, пока значение не равно None.
            string=string+str(head.val) #записываем значение в строку (через строчный метод).
            head=head.next #перезаписываем текущее значение на следущий элемент.
        return int(string, 2) #возращаем значение в 10 СС.