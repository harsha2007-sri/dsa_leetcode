class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        """l,r=len(needle),0
        found=False
        if len(haystack)==len(needle):
            return 0
        for i in range(l,len(haystack)):
            if haystack[r:i]==needle:
                found=True
                break
            r+=1

        return r if found else -1"""
        
        k = len(needle)
        for i in range(len(haystack)-k+1):
            if haystack[i:i+k] == needle:
                return i
            
        return -1
