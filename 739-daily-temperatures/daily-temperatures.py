class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        n = len(temperatures)
        answer = [0] * n

        #Brute force = for each day we will scan forward in the array
        # O(n^2)

        stack = []

        for currDay in range(n):
            currTemp = temperatures[currDay]

            while stack and temperatures[stack[-1]] < currTemp:
                prevDay = stack.pop()
                answer[prevDay] = currDay - prevDay

            stack.append(currDay)

        return answer

        


        
        