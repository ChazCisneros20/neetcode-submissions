# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        s = 1
        e = n
        while s<=e:
            mid = (s+e)//2
            if guess(mid) < 0:
                #// If target is less than mid
                e = mid - 1
            elif guess(mid) > 0:
                s = mid + 1
            else:
                return mid 
        return -1
        
            
