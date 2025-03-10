class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # window length = (R - L) + 1

        s_char_set = set()
        l = 0
        longest = 0

        for r in range(len(s)):
            while s[r] in s_char_set:
                s_char_set.remove(s[l])
                l += 1
                # s_char_set.add(s[r])
            
            window = (r - l) + 1
            longest = max(longest, window)
            s_char_set.add(s[r])


        return longest

        #time complexity : o(n)
        #space : O(n) as we are using set
        