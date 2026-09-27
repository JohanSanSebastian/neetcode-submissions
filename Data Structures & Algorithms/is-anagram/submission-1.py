class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash1 = {}
        hash2 = {}
        for let in list(s):
            try:
                hash1[let] += 1
            except:
                hash1[let] = 0
        for let2 in list(t):
            try:
                hash2[let2] += 1
            except:
                hash2[let2] = 0
        if hash1 == hash2:
            return True
        
        return False
