class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        result = []
        max_candy = max(candies)

        for candy in candies:
            if candy + extraCandies >= max_candy:
                result.append(True)
            else:
                result.append(False)
        
        return result