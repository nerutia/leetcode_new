#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.st = []
        self.rank = []  # 始终存此次push后的最小值，一路存。


    def push(self, val: int) -> None:
        self.st.append(val)
        v = self.rank[-1] if self.rank else float("inf")
        self.rank.append(min(v, val))

    def pop(self) -> None:
        self.rank.pop()
        return self.st.pop()


    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.rank[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

