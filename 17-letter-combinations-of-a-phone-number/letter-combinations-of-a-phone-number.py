class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone_map = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        if not digits:
            return []

        queue = deque([""])

        for digit in digits:
            letters = phone_map[digit]
            size = len(queue)
            for _ in range(size):
                combination = queue.popleft()
                for letter in letters:
                    queue.append(combination + letter)
        return list(queue)

        

        