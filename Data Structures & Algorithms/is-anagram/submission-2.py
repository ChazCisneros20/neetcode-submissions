class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap_s = {}
        hashMap_t = {}
        for letter in s:
            if letter not in hashMap_s:
                hashMap_s[letter] = 1
            else:
                hashMap_s[letter]+=1
        for letter in t:
            if letter not in hashMap_t:
                hashMap_t[letter] = 1
            else:
                hashMap_t[letter]+=1
        for key,val in hashMap_s.items():
            if key not in hashMap_t or hashMap_s[key] != hashMap_t[key]:
                return False 
        for key,val in hashMap_t.items():
            if key not in hashMap_s or hashMap_t[key] != hashMap_s[key]:
                return False
        return True 

            
        
