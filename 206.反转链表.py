#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        迭代
        if head == None:
            return None
        p, r = None, head
        while r.next:
            t = r.next
            r.next = p
            p = r
            r = t
        r.next = p
        return r
        # 大佬做法：
        # p, rev = head, None
        # while p:
        #     rev, rev.next, p = p, rev, p.next
        # return rev
        # 递归：
        # if head is None or head.next is None:
        #     return head
        # new_head = self.reverseList(head.next) # 反转后的链表表头
        # head.next.next = head
        # head.next = None
        # return new_head
# @lc code=end

