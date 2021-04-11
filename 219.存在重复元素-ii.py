#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#
from typing import List
# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        k += 1
        s = set(nums[:k])
        if len(s) < len(nums[:k]):
            return True
        for i in range(k, len(nums)):
            s.remove(nums[i-k])
            s.add(nums[i])
            if len(s) < k:
                return True
        return False
# @lc code=end

