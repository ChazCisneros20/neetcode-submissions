class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack1 = []
        stack2 = []
        for operation in operations:
            #Will always be 2 previous records in stack1
            #And 1 previous record in stack2
            if operation == "+":
                summedValue = stack1[-1] + stack2[-1]
                stack2.append(stack1[-1])
                stack1.append(summedValue)
                
            #At minimum 1 prev record in stack1
            elif operation == "C":
                #If stack1 has 2+ and stack1 is 1+
                if len(stack1) > 1:
                    del stack1[-1]
                    del stack2[-1]
                else:
                    del stack1[-1]
            #At minimum 1 prev record in stack1
            elif operation == "D":
                stack2.append(stack1[-1])
                stack1.append(stack1[-1]*2)
                
            else:
                if len(stack1) == 0:
                    stack1.append(int(operation))
                    #Leave stack2 alone.
                else:
                    #stack2 has the top() of stack1 before stack1 gets new push
                    stack2.append(stack1[-1])
                    stack1.append(int(operation))
        return sum(stack1)
