class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        count=0
        x=str(x)
        if x[0]=="-":
            count+=1
        if count==0:
            y=x[::-1]
            if x==y:
                return True
        else:
            y='-'
            y=y+x[:1:-1]
            if x==y:
                return True
        return False

        

        
