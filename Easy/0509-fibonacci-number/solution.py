class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        elif n in [1,2]:
            return 1
        return self.fib(n-1)+self.fib(n-2)
        
