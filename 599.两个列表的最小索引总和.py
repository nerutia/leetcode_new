'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-09 00:24:32
LastEditors: hqh
LastEditTime: 2021-05-09 01:08:50
'''
#
# @lc app=leetcode.cn id=599 lang=python3
#
# [599] 两个列表的最小索引总和
#

# @lc code=start
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        c = set(list1) & set(list2)
        d = {}
        for idx, val in enumerate(list1):
            if val not in d:
                d[val] = idx
        for idx, val in enumerate(list2):
            if val in d:
                d[val] += idx
        r, v = [], -1
        for i, j in d.items():
            if i not in c:
                continue
            if v == -1 or v == j:
                v = j
                r.append(i)
            elif v > j:
                v = j
                r = [i]
        return r


# @lc code=end
