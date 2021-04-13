#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#
from typing import List
# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        r = []
        for i in nums1:
            if i in nums2:
                r.append(i)
                nums2.remove(i)
        return r
        # 大佬
        # return  list((collections.Counter(nums1) & collections.Counter(nums2)).elements())
        # 最快是排序+双指针
# @lc code=end

