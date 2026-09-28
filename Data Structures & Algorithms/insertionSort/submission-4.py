# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if len(pairs) == 0:
            return [] 
        res = [] 
        res.append(pairs.copy())
        for i in range(1, len(pairs)):
            j = i-1 #// we always check the prior value and the curr value
            while j >= 0 and pairs[j+1].key < pairs[j].key: #// if the element in front of j is LESS than j 
                #// SWAP 
                temp = pairs[j]
                pairs[j] = pairs[j+1]
                pairs[j+1] = temp 
                #// DECREMENT J and swap until the inserted value is in the correct spot.
                j-=1
            res.append(pairs.copy())
        return res 
        
