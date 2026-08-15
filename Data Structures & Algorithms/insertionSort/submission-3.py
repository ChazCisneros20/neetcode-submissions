# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

#THIS IS STABLE AND THE QUESTION DOES NOT WANT RECORDINGS FOR EACH INSERTION.
#RECORD AFTER EACH OUTER LOOP. 
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        states = []
        if len(pairs) == 0:
            return states
        states.append(pairs.copy())
        #n = len(pairs)
        for i in range(1, len(pairs)):
            j = i
            while j > 0 and (pairs[j-1].key > pairs[j].key):
                pairs[j-1], pairs[j] = pairs[j], pairs[j-1]
                
                j-=1
            states.append(pairs.copy())
        return states 