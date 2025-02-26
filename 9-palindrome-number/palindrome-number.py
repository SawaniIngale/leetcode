class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        original = x
        reversed_num = 0
        while x!= 0:
            pop = x % 10
            x //= 10
            reversed_num = reversed_num * 10 + pop
        return original == reversed_num  