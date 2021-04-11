#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # while head and head.val == val:  # 找到第一个值不为val的节点
        #     head = head.next
        # if head:  # 递归
        #     head.next = self.removeElements(head.next, val)
        # return head
        while head:
            if head.val == val:
                head = head.next
            else:
                head.next = self.removeElements(head.next, val)
                return head
# @lc code=end

