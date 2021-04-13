#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p = len(nums)
        for i in range(p):
            if nums[i] == 0:
                p = i
                break
        l = p
        for i in range(l, len(nums)):
            if nums[i] != 0:
                nums[p], nums[i], p = nums[i], 0, p + 1
        # 大佬
        # nums.sort(key=bool, reverse=True)
# @lc code=end

