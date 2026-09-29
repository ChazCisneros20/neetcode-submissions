#Input: piles = [1,4,3,2], h = 9
#Says: 1//k 

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # find our max(p)
        maxp = piles[0]
        for pile in piles:
            if pile > maxp:
                maxp = pile 
        start = 1 
        end = maxp 
        def binarySearch(startK, endK):
            if (endK-startK+1) <= 1:
                return startK
            midK = (startK + endK)//2

            total = 0 
            for pile in piles:
                total += -(-pile//midK) #// ceiling division 
            if total <= h:
                return binarySearch(startK, midK)
            else:
                return binarySearch(midK+1, endK)
        return binarySearch(start, end)


            
            

        

        
