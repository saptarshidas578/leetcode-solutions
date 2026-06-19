1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def pairSum(self, head: Optional[ListNode]) -> int:
8        l=[]
9        while head is not None:
10            l.append(head.val)
11            head=head.next
12        s=l[::-1]
13        for i in range(len(s)):
14            s[i]=s[i]+l[i]
15        return max(s)
16
17        