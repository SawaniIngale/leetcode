class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #Brute force O(n^3)

        # result = 0
        # n = len(nums)

        # for i in range(n):
        #     for j in range(i+1, n):
        #         for k in range(j+1, n):
        #             value = (nums[i] - nums[j]) * nums[k]
        #             result = max(result, value)

        # return result 

        #Greedy method

        result = 0
        max_diff = 0
        max_value = 0

        for num in nums:
            result = max(result, max_diff * num)
            max_diff = max(max_diff, max_value - num)
            max_value = max(max_value, num)

        return result




