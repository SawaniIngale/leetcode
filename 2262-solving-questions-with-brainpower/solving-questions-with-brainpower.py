class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        n = len(questions)
        dp = [0] * (n+1)
        next_val = 0

        for i in range(n-1, -1, -1):
            points, brainpower = questions[i]
            next_q = i + brainpower + 1
            dp[i] = max(points + (dp[next_q] if next_q < n else 0), dp[i+1])
            next_val = dp[i]

        return next_val
        