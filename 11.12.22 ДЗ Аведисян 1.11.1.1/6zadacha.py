# Сложность O(n)
class Solution:
    def hasCycle(self, head):
        firstik=head
        secondik=head
        while secondik and secondik.next:
            firstik=firstik.next
            secondik=secondik.next
            if firstik==secondik:
                return True
        return False