'''
Author: your name
Date: 2021-04-25 21:01:00
LastEditTime: 2021-04-26 00:17:09
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \tmp\506.相对名次.py
'''
#
# @lc app=leetcode.cn id=506 lang=python3
#
# [506] 相对名次
#
from typing import List
# @lc code=start
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        idx = list(range(len(score)))
        res = list(range(len(score)))
        for i in res:
            res[i] = str(i+1)
            if i == 0:
                res[i] = 'Gold Medal'
            if i == 1:
                res[i] = 'Silver Medal'
            if i == 2:
                res[i] = 'Bronze Medal'
        idx = list(zip(*sorted(zip(score, idx), key=lambda x:-x[0])))[1]
        return list(zip(*sorted(zip(idx, res), key=lambda x:x[0])))[1]
        # 大佬
        # d = {n: i + 1 for i, n in enumerate(sorted(nums, reverse=True))}
        # b = {1: 'Gold Medal', 2: 'Silver Medal', 3: 'Bronze Medal'}
        # for i, n in enumerate(nums):
        #     a = d[n]
        #     nums[i] = b[a] if a < 4 else str(a)
        # return nums
# @lc code=end

s = Solution()
s.findRelativeRanks([1,3,2,4,7,6,5])