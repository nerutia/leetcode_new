#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#

# @lc code=start
class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.front = []
        self.end = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if len(self.end) != 0 or len(self.front) == 0:
            return self.end.append(x)
        while len(self.front) > 0:
            self.end.append(self.front.pop())
        self.end.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.front) != 0:
            return self.front.pop()
        while len(self.end) > 1:
            self.front.append(self.end.pop())
        return self.end.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        t = self.pop()
        self.front.append(t)
        return t


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.front) == 0 and len(self.end) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

