class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        l=0
        n=len(s1)
        m=len(s2)
        if n>m:
            return False
        count1={}   
        for ch in s1:
            count1[ch]=count1.get(ch,0)+1 
        count2={}
        for i in range(n):
            ch=s2[i]
            count2[ch]=count2.get(ch,0)+1    
        if count1==count2:
            return True
        for r in range(n,m):
            count2[s2[l]]-=1
            if count2[s2[l]]==0:
                del count2[s2[l]]
            count2[s2[r]]=count2.get(s2[r],0)+1
            l+=1
            if count1==count2:
                return True
        return False