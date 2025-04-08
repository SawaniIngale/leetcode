class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        for i in range(len(nums)-1,-1,-1):
            if nums[i] in seen:
                return (i//3)+1
            else:
                seen.add(nums[i])
        return 0



        