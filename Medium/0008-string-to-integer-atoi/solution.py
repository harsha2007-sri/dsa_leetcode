class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.strip()
        if not s:
            return 0
        else:
            sign = 1
            i = 0
            if s[0]=="-":
                sign = -1
                i = 1
            elif s[0]=="+":
                i=1
            ans=0
            while i<len(s) and s[i].isdigit():
                ans=ans*10+int(s[i])
                i+=1
            ans*=sign
            if ans<-2**31:
                ans=-2**31
            if ans>2**31-1:
                ans=2**31-1
            return ans
