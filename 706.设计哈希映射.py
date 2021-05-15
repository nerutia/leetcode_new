'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-15 23:27:01
LastEditors: hqh
LastEditTime: 2021-05-15 23:29:13
'''
#
# @lc app=leetcode.cn id=706 lang=python3
#
# [706] 设计哈希映射
#

# @lc code=start
class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.d[key] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if key in self.d:
            return self.d[key]
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key in self.d:
            del self.d[key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end
