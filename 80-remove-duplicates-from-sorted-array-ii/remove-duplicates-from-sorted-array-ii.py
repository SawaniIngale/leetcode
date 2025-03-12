class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0
        
        dup = 1

        i = 0
        for j in range(1,len(nums)):
            if nums[j] == nums[i]:
                dup += 1

            else:
                dup = 1

            if dup <= 2:
                i += 1
                nums[i] = nums[j]
                
        return i+1

        
        