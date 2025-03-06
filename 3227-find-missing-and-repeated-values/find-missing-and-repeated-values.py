class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n = len(grid)
        count = {i:0 for i in range(1, n*n + 1)}

        for row in grid:
            for num in row:
                count[num] += 1

        duplicate, missing = -1, -1
        for num in count:
            if count[num] == 2:
                duplicate = num
            elif count[num] == 0:
                missing = num

        return [duplicate, missing]