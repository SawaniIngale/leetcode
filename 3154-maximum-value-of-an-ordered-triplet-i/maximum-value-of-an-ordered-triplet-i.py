class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_prefix = 0
        max_diff = 0
        max_value = 0

        for num in nums:
            max_value = max(max_value, max_diff * num)
            max_diff = max(max_diff, max_prefix - num)
            max_prefix = max(max_prefix, num)

        return max_value

            