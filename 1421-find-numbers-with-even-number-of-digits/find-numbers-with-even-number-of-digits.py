class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for x in nums:
            digits = 0
            while x > 0:
                digits += 1
                x //= 10

            if (digits & 1) == 0:
                count += 1
                
        return count
        