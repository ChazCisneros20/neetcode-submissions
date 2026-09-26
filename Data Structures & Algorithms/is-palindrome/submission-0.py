class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        i=0
        j=n-1
        while i < j:
            left_char = s[i].lower()
            right_char = s[j].lower()
            if left_char.isalnum() and right_char.isalnum():
                if left_char != right_char:
                    return False 
                j-=1
                i+=1
            elif left_char.isalnum():
                j-=1
            elif right_char.isalnum():
                i+=1
            else:
                i+=1
                j-=1
        return True  
