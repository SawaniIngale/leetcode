class Solution(object):
    def minCapability(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def canRob(maxValue):
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= maxValue:  # Can rob this house
                    count += 1
                    i += 2  # Skip the next house to avoid adjacent issues
                else:
                    i += 1
            return count >= k

        # Binary Search on possible house values
        left, right = min(nums), max(nums)
        while left < right:
            mid = (left + right) // 2
            if canRob(mid):
                right = mid  # Try a smaller maximum value
            else:
                left = mid + 1  # Increase the maximum value
        return left




        