#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # r = []
        # while head:
        #     r.append(head.val)
        #     head = head.next
        # return r == r[::-1]
        if not head:
            return True
        fast, slow = head, head
        while fast:
            slow = slow.next
            fast = fast.next.next if fast.next else None
        c, p = slow, None
        while c:
            # 虽然是并行，但是是挨个赋值的，
            # 只不过右侧的值保持为赋值前的值
            p, p.next, c = c, p, c.next
        while p:
            if p.val != head.val:
                return False
            p = p.next
            head = head.next
        return True
# @lc code=end

