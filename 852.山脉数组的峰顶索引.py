'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-18 22:27:10
LastEditors: hqh
LastEditTime: 2021-05-18 22:34:05
'''
#
# @lc app=leetcode.cn id=852 lang=python3
#
# [852] 山脉数组的峰顶索引
#

# @lc code=start
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # for i in range(1, len(arr) - 1):
        #     if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
        #         return i
        l, r = 1, len(arr) - 1
        while l <= r:
            m = l + (r - l) // 2
            if arr[m] > arr[m - 1] and arr[m + 1] > arr[m]:
                l = m + 1
            elif arr[m] < arr[m - 1] and arr[m + 1] < arr[m]:
                r = m - 1
            else:
                return m
        # 大佬
        # return arr.index(max(arr))


# @lc code=end
