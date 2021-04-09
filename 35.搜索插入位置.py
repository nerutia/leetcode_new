#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        m, M = 0, len(nums) - 1
        while m <= M:
            mid = (m + M) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                m = mid + 1
            if nums[mid] > target:
                M = mid - 1
        return m  # 注意这里返回m，而前面返回mid

# @lc code=end

