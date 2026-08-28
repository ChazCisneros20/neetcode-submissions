class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        concat=[]
        for i in range(len(matrix)):
            concat += matrix[i]
        s = 0 
        e = len(concat)-1
        while s <= e:
            m = (s+e)//2
            if concat[m] == target:
                return True
            elif target < concat[m]:
                e = m - 1
            else:
                s = m + 1
        return False 