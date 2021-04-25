#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set(range(1, len(nums) + 1)) - set(nums))
        # 进阶不会，下面是大佬
        # 将所有正数作为数组下标，置对应数组值为负值。
        # 那么，仍为正数的位置即为（未出现过）消失的数字。
        # 举个例子：
        # 原始数组：[4,3,2,7,8,2,3,1]
        # 重置后为：[-4,-3,-2,-7,8,2,-3,-1]
        # 结论：[8,2] 分别对应的index为[5,6]（消失的数字）
        # for num in nums:
        #     nums[abs(num)-1] = -abs(nums[abs(num)-1])
        # print(nums)
        # return [i+1 for i,num in enumerate(nums) if num>0]
# @lc code=end

