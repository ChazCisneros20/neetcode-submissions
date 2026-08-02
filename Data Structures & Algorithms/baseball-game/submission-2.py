class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for operation in operations:
            #Will always be 2 previous records in stack1
            #And 1 previous record in stack2
            if operation == "+":
                a = stack[-1]
                del stack[-1]
                b = stack[-1]
                del stack[-1]
                #then push b and a back.
                summed_value = a + b
                stack.append(b)
                stack.append(a)
                stack.append(summed_value)

            #At minimum 1 prev record in stack1
            elif operation == "C":
                #If stack1 has 2+ and stack1 is 1+
                del stack[-1]
            #At minimum 1 prev record in stack1
            elif operation == "D":
                stack.append(stack[-1] * 2)
                
            #If push(number) ->
            else:
                stack.append(int(operation))
        return sum(stack)
