'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-15 22:35:48
LastEditors: hqh
LastEditTime: 2021-05-15 23:04:15
'''
#
# @lc app=leetcode.cn id=703 lang=python3
#
# [703] 数据流中的第 K 大元素
#

# @lc code=start
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        t = sorted(nums)
        t = t[::-1]
        self.arr = t[:k]

    def add(self, val: int) -> int:
        for i in range(min(self.k, len(self.arr))):
            if self.arr[i] < val:
                self.arr.insert(i, val)
                break
        else:
            self.arr.append(val)
        return self.arr[self.k - 1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end
