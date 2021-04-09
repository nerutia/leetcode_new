#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        t = [nums[0]]  # 建表，存到此位置为止最大和
        for i in range(1, len(nums)):
            t.append(max(t[i-1] + nums[i], nums[i]))
        return max(t)
        # r = nums[0]  # 存最大和
        # t = 0  # 存暂时最大和
        # for v in nums:
        #     if t + v > 0:
        #         t += v
        #         r = max(r, t)
        #     else:
        #         r = max(r, v)
        #         t = 0
        # return r
# @lc code=end

