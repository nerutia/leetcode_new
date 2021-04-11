#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 摩尔投票法
        t = 1
        c = nums[0]
        for i in range(1, len(nums)):
            v = nums[i]
            if c == v:
                t += 1
            elif t == 0:
                c = v
                t = 1
            else:
                t -= 1
        return c
        # 其他：
        # 因为一定有众数，且众数个数大于n/2，
        # 所以直接排序输出n/2位置的数即可
# @lc code=end

