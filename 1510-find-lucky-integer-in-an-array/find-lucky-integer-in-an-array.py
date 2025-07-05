class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        counts = Counter(arr)
        res = -1

        for num, cnt in counts.items():
            if num == cnt:
                res = max(res, num)
        return res

        