#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
#

# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        self.s = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                self.s[i] = nums[i]
            else:
                self.s[i] = self.s[i-1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.s[right]
        return self.s[right] - self.s[left - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end

