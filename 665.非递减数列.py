'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-11 13:10:24
LastEditors: hqh
LastEditTime: 2021-05-11 13:30:11
'''
#
# @lc app=leetcode.cn id=665 lang=python3
#
# [665] 非递减数列
#

# @lc code=start
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        t = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if i == 0:
                    nums[0] = nums[1]
                    t = True
                    continue
                if nums[i - 1] > nums[i + 1]:
                    nums[i + 1] = nums[i]
                    if t:
                        return False
                    t = True
                elif nums[i - 1] <= nums[i + 1]:
                    nums[i] = nums[i - 1]
                    if t:
                        return False
                    t = True
                else:
                    return False
        return True


# @lc code=end
