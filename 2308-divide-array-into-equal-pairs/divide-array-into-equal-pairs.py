class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        count = Counter(nums)

        for cnt in count.values():
            if cnt % 2 != 0:
                return False
        return True
        