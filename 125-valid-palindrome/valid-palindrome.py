import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # updated = ''.join(char.lower() for char in s if char.isalnum())

        # l, r = 0, len(updated) - 1
        # while l < r:
        #     if updated[l] != updated[r]:
        #         return False
        #     l += 1
        #     r -= 1

        # return True

        # Using regular expression

        updated = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return updated == updated[::-1]

        