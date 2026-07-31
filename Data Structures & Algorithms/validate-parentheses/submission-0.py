class Solution:
    def isValid(self, s: str) -> bool:
        ValidParenthesesBucket = []
        for bracket in s:
            print(bracket)
            if bracket == '(' or bracket == '[' or bracket ==  '{':
                print('im [({')
                ValidParenthesesBucket.append(bracket)
            else:
                print('im ])}')
                if len(ValidParenthesesBucket) > 0:
                    #pop
                    
                    if ValidParenthesesBucket[len(ValidParenthesesBucket) -1] == '(' and bracket == ')':                     
                        del ValidParenthesesBucket[len(ValidParenthesesBucket) - 1]
                    elif ValidParenthesesBucket[len(ValidParenthesesBucket) -1] == '[' and bracket == ']':                 
                        del ValidParenthesesBucket[len(ValidParenthesesBucket) - 1]
                    elif ValidParenthesesBucket[len(ValidParenthesesBucket) -1] == '{' and bracket == '}':                     
                        del ValidParenthesesBucket[len(ValidParenthesesBucket) - 1]
                    else: return False
                else:
                    #This means the bucket is empty and already given an invalid paranthesis
                    return False
        if len(ValidParenthesesBucket) == 0:
            return True
        else:
            return False