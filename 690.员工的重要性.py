'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-14 11:42:33
LastEditors: hqh
LastEditTime: 2021-05-15 21:49:29
'''
#
# @lc app=leetcode.cn id=690 lang=python3
#
# [690] 员工的重要性
#

# @lc code=start
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        d = {}
        for i in employees:
            d[i.id] = [i.importance, i.subordinates]
        r = 0
        st = [d[id]]
        while st:
            rt = st.pop(0)
            r += rt[0]
            if rt[1]:
                for i in rt[1]:
                    st.append(d[i])
        return r
        # 大佬：
        # d = {e.id: e for e in employees}
        # def f(i):
        #     e = d[i]
        #     return e.importance + sum(map(f, e.subordinates))
        # return f(id)


# @lc code=end
