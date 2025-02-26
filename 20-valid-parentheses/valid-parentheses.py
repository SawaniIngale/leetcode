class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        matching_brackets = { ')' : '(', '}' : '{', ']' : '['}
        stack = []

        for char in s:
            if char in matching_brackets:
                top_ele = stack.pop() if stack else '#'

                if matching_brackets[char] != top_ele:
                    return False
            else:
                stack.append(char)
            
        return not stack
