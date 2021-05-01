'''
Author: your name
Date: 2021-04-25 19:43:49
LastEditTime: 2021-04-25 19:59:38
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \tmp\496.下一个更大元素-i.py
'''
#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        for idx, val in enumerate(nums2):
            for i in range(idx + 1, len(nums2)):
                if nums2[i] > val:
                    d[val] = nums2[i]
                    break
            else:
                d[val] = -1
        return [d[i] for i in nums1]
# @lc code=end

