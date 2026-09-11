class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1={}
        dict2={}
        for v1 in s:
            if v1 in dict1:
                dict1[v1]+=1
            else:
                dict1[v1]=1
            
        for v2 in t:
            
            if v2 in dict2:
                dict2[v2]+=1
            else:
                dict2[v2]=1
        for key in dict1.keys():
            if key not in dict2.keys():
                return False
            if dict1[key] != dict2[key]:
                return False 
        for key in dict2.keys():
            if key not in dict1.keys():
                return False
            if dict2[key] != dict1[key]:
                return False 
        return True