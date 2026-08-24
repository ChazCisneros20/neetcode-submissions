class Solution:
    def initialize(self):
        table = [0]*256
        for i in range(256):
            #Get the LSB (odd/even) bit, then recursively imagine getting the n>>1 (1101 -> 110) bits as they
            #were precomputed
            table[i] = (i & 1) + table[i//2]
        
        return table
    def countBits(self, n: int) -> List[int]:
        table = self.initialize()
        output = []
        for i in range(0, n+1):
            count=0
            bitsToShift=0
            for j in range(4):
                count += table[(i>>bitsToShift) & 0xff]
                bitsToShift+=8
            output.append(count)
        return output
        
        