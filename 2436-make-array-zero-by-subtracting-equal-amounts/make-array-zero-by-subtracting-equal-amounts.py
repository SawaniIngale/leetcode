class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = 0
        while any(nums):
            min_val = min([num for num in nums if num > 0])
            nums = [num - min_val if num > 0 else 0 for num in nums]
            count += 1

        return count
        