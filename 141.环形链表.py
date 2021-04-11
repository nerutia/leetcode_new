#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast, slow = head, head
        while fast:
            fast = fast.next
            if fast == None:
                break
            fast = fast.next
            slow = slow.next
            if fast == slow:
                break
        return not (fast == None)
# @lc code=end

