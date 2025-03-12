class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        even_count = 0
        odd_count = 0

        for num in nums:
            if num > 0:
                even_count += 1
            elif num < 0:
                odd_count += 1
        return max(even_count, odd_count)
