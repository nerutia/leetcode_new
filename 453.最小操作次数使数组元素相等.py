#
# @lc app=leetcode.cn id=453 lang=python3
#
# [453] 最小操作次数使数组元素相等
#

# @lc code=start
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - min(nums) * len(nums)
# @lc code=end




# class Node:
#     def __init__(self, val, nn=None):
#         self.val = val
#         self.next = nn


# head = Node(1, Node(2, Node(3, Node(4))))

# p = head

# while p and p.next:
#     p = p.next

# print(p.val)