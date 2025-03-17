class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(" ", "")
        num = 0
        sign = '+'
        stack = []

        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)

            if char in '+-*/' or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    top = stack.pop()
                    if top < 0:
                        stack.append(-(-top // num))  # Proper rounding for negatives
                    else:
                        stack.append(top // num)


                num = 0
                sign = char

        return sum(stack)

