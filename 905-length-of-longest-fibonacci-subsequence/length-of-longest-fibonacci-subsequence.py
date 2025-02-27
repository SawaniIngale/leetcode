class Solution(object):
    def lenLongestFibSubseq(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr_set = set(arr)
        result = 0

        for i in range(len(arr) - 1):
            for j in range(i+1, len(arr)):
                prev, curr = arr[i], arr[j]
                nxt = prev + curr
                length = 2
                while nxt in arr_set:
                    length += 1
                    prev, curr = curr, nxt
                    nxt = prev + curr
                    result = max(result, length)
        return result
        