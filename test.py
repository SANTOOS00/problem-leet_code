# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res1 = 0
        res2 = 0
        while (l1 or l2):
            if (l1):
                res1 = res1 * 10 + l1.val
                l1 = l1.next
            if (l2):
                res2 = res2 * 10 + l2.val
                l2 = l2.next
        res = res1 + res2
        i = 0
        while (res):
            res = res // 10
            i += 1
        head = ListNode()
        while (i):
            

node1 = ListNode(2)
node2 = ListNode(4)
node3 = ListNode(3)

node4 = ListNode(5)
node5 = ListNode(6)
node6 = ListNode(4)

node1.next = node2
node2.next = node3

node4.next = node5
node5.next = node6

# print(node1.val)
SS = Solution()
SS.addTwoNumbers(node1, node4)