class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}
        for value in nums:
            if value in my_dict:
                my_dict[value]+=1
            else:
                my_dict[value]=1
        for k,v in my_dict.items():
            if v > 1:
                return True 
        return False 
