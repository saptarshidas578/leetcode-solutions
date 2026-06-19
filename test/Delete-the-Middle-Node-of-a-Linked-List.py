1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        if head.next is None:
9            return None
10        fast=head
11        slow= head
12        prev=None
13        while fast and fast.next:
14            fast=fast.next.next
15            prev=slow
16            slow= slow.next
17        prev.next=slow.next
18        return head
19       
20       
21        