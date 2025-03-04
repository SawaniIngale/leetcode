class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #brute force that can handle edge cases : Time complexity O(n^2) as we are traversing through all elements in O(n) and then taking the min for which we have to scan the whole array in O(n)
        # count = 0
        # while any(nums):
        #     min_val = min([num for num in nums if num > 0])
        #     nums = [num - min_val if num > 0 else 0 for num in nums]
        #     count += 1

        # return count

        # Optimized approach using sets: Sets will give us unique elements and if we minus the 0's then we have unique numbers whose length will the number of operations needed to make all elements to 0 : Time complexity o(n)
        # set(nums): O(n) to create a set,  -{0} O(1) to remove zeros, len(set) O(1)

        return len(set(nums) - {0})

        