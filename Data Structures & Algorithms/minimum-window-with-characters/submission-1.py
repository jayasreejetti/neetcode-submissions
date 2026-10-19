class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s)<len(t):
            return ""
        need={}
        for ch in t:
            need[ch]=need.get(ch,0)+1
        win={}
        have=0
        req=len(need)

        l=0
        min_len=float("inf")
        start=0

        for r in range(len(s)):
            ch=s[r]
            win[ch]=win.get(ch,0)+1
            if ch in need and win[ch]==need[ch]:
                have+=1
            while have==req:
                if r-l+1<min_len:
                    min_len=r-l+1
                    start=l
                left_ch=s[l]
                win[left_ch]-=1
                if left_ch in need and win[left_ch]<need[left_ch]:
                    have-=1

                l+=1
        if min_len==float("inf"):
            return ""
        return s[start:start+min_len]



        