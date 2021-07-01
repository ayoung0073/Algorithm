# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def nodeToInt(l):
    q = deque()
    while l != None:
        q.appendleft(l.val)
        l = l.next
    return int(''.join(str(i) for i in list(q)))

# 76 ms	14.4 MB
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
      
