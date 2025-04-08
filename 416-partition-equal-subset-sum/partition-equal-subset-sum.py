class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
    
        if total % 2 != 0:
            return False
        
        target = total // 2
        n = len(nums)
        
        dp = [False] * (target + 1)
        dp[0] = True  # Base case: zero can always be formed
        
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        
        return dp[target]
        