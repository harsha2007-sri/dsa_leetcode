class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """s=s.lower()
        a=""
        for i in s:
            if i.isalnum():
                a+=i
        return True if a==a[::-1] else False
        """
        s=s.lower()
        low=0
        high=len(s)-1
        while low<=high:
            while low<high and not s[low].isalnum():
                low+=1
            while low<high and not s[high].isalnum():
                high-=1
            if s[low]!=s[high]:
                return False
            else:
                low+=1
                high-=1
        return True
        
