# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def nodeToInt(l):
    num = 0
    mul = 1
    while l:
        num += l.val * mul
        mul *= 10
        l = l.next
    return num

# 76 ms	14.4 MB -> 68 ms 14.2 MB
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = nodeToInt(l1)
        num2 = nodeToInt(l2)
        val = str(num1 + num2)
        
        node = ListNode()
        head = None
        for num in reversed(val):
            if not head:
                head = ListNode(int(num))
                node = head
            else:
                node.next = ListNode(int(num))
                node = node.next
            
        return head
      
