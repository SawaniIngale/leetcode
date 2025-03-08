class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """

        min_white = blocks[:k].count('W')
        curr_white = min_white

        for i in range(k, len(blocks)):
            if blocks[i-k] == 'W':
                curr_white -= 1
            if blocks[i] == 'W':
                curr_white += 1

            min_white = min(min_white, curr_white)

        return min_white

        