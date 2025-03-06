class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n = len(grid)
        count = {i:0 for i in range(1, n*n + 1)}
       # n = 2 , range = (1,5)
       # count = {1:0, 2:0, 3:0, 4:0}

        for row in grid: # for each row
            for num in row: # for every num in that particular row
                count[num] += 1 

        duplicate, missing = -1, -1 #Not setting to 0 to not mislead
        for num in count:
            if count[num] == 2:
                duplicate = num
            elif count[num] == 0:
                missing = num

        return [duplicate, missing]