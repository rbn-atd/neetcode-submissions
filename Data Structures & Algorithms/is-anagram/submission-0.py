class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sx = {}
        tx = {}
        for i in s:
            if i in sx:
                sx[i] += 1
            else:
                sx[i] = 1
        for i in t:
            if i in tx:
                tx[i] += 1
            else:
                tx[i] = 1
        
        if sx == tx:
            return True
        else:
            return False