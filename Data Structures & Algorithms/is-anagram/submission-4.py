class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        counts={}
        countt={}
        for char in s:
            counts[char]=counts.get(char,0)+1
        for char in t:
            countt[char]=countt.get(char,0)+1
        return counts == countt