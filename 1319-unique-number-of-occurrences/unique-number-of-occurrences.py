class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        counter = Counter(arr)
        s = set()

        for v in counter.values():
            if v in s:
                return False
            else:
                s.add(v)

        return True
        