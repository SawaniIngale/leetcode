class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        # stack = []
        # for token in tokens:
        #     if token.lstrip('-').isdigit():
        #         stack.append(int(token))
        #     else:
        #         b = stack.pop()
        #         a = stack.pop()
        #         if token == '+':
        #             stack.append(a+b)
        #         elif token == '-':
        #             stack.append(a-b)
        #         elif token == '*':
        #             stack.append(a*b)
        #         elif token == '/':
        #             if 
        #             stack.append(int(a/b))

        # return stack[0]
        # stack = []
        
        # for token in tokens:
        #     if token.lstrip('-').isdigit():  # Handle negative numbers
        #         stack.append(int(token))
        #     else:
        #         b = stack.pop()
        #         a = stack.pop()
                
        #         if token == '+':
        #             stack.append(a + b)
        #         elif token == '-':
        #             stack.append(a - b)
        #         elif token == '*':
        #             stack.append(a * b)
        #         elif token == '/':
        #             result = a // b if a * b >= 0 else (a // b + 1 if a % b != 0 else a // b)
        #             stack.append(result)
        
        # return stack[0] 

        stack = []
        for t in tokens:
            if t not in {"+","-","*","/"}:
                stack.append(int(t))

            else:
                num2 = stack.pop()
                num1 = stack.pop()

                if t == '+':
                    stack.append(num1+num2)
                elif t == '-':
                    stack.append(num1 - num2)
                elif t == '*':
                    stack.append(num1 * num2)
                elif t == '/':
                    result = abs(num1) // abs(num2)
                    if (num1 < 0) ^ (num2 < 0):
                        result = -result
                    stack.append(result)
        return stack[-1]       