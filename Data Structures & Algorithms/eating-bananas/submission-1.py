#Input: piles = [1,4,3,2], h = 9
#Says: 1//k 

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max = piles[0]
        for pile in piles:
            if pile >= max:
                max = pile 
        
        s = 1 
        e = max
        res = 0 
        #// L and R should never corss eachother
        
        #If this is 1-11 the mid will be k=6
        while s <= e:
            midK = (s+e)//2
            count = 0
            for pile in piles:
                #// Sum up the ceiling division of the pile/k bananas per hour 
                count += -(-pile//midK)
            
            #// If count is TOO HIGH, it means we are too far left, 
            #// So we should look right. 
            if count <= h:
                res = midK
                e = midK - 1 
            else:
                s = midK + 1
        return res

            
            

        

        
