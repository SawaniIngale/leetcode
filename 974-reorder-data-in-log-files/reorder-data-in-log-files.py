class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letter_logs = []
        digit_logs = []

        for log in logs:
            if log.split()[1].isdigit():
                digit_logs.append(log)

            else:
                letter_logs.append(log)


        #Sorting the Letter logs by lexicographically arranging the content, if the content is same then it will be sorted with the help of identifier
        letter_logs.sort(key = lambda x: (x.split(' ',1)[1], x.split(' ',1)[0]))

        return letter_logs + digit_logs