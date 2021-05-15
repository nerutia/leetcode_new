'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-15 23:13:08
LastEditors: hqh
LastEditTime: 2021-05-15 23:26:14
'''
#
# @lc app=leetcode.cn id=705 lang=python3
#
# [705] 设计哈希集合
#

# @lc code=start
class MyHashSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}

    def add(self, key: int) -> None:
        self.d[key] = True

    def remove(self, key: int) -> None:
        self.d[key] = False

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key not in self.d:
            return False
        return self.d[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end
