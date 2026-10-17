class Solution(object):
    def isFascinating(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s=str(n)+str(n*2)+str(n*3)
        if len(s)!=9:
            return False
        if "0" in s:
            return False
        if len(set(s))==9:
            return True
        else:
            return False
