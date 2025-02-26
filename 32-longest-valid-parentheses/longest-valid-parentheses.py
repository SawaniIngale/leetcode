class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        stack = [-1]
        length = 0

        for i,char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    length = max(length, i - stack[-1])
                else:
                    stack.append(i)
        return length

        