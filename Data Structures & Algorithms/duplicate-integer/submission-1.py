class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}
        for num in nums:
            if num not in my_dict:
                my_dict[num] = 1
            else:
                my_dict[num]+=1
        for k,v in my_dict.items():
            if v > 1:
                return True 
        return False 