class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # word = s.split()
        # return len(word[-1])

        #-------- to do inplace iterating from end

        i = len(s)-1

        while i >= 0 and s[i] == " ":
            i -= 1
        length = 0
        while i >= 0 and s[i]!= " ":
            length += 1
            i -= 1

        return length



        