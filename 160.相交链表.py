#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        def getlen(r):
            l = 0
            while r:
                l += 1
                r = r.next
            return l
        l1 = getlen(headA)
        l2 = getlen(headB)
        r1 = headA
        r2 = headB
        while l1 > l2:
            r1 = r1.next
            l1 -= 1
        while l1 < l2:
            r2 = r2.next
            l2 -= 1
        while r1 != r2:
            r1 = r1.next
            r2 = r2.next
        return r1
        # 大佬做法
        # 定义两个指针, 第一轮让两个到达末尾的节点指向另一个链表的头部,
        # 最后如果相遇则为交点(在第一轮移动中恰好抹除了长度差)
        # 两个指针等于移动了相同的距离, 有交点就返回,
        # 无交点就是各走了两条指针的长度
# @lc code=end

