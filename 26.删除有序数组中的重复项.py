#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 1
        while len(nums) > p:
            if nums[p] == nums[p-1]:
                nums.pop(p)
            else:
                p += 1
        return len(nums)
# @lc code=end

