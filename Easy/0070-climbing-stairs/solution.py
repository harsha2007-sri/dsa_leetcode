class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum=1
        p_sum=0
        fib=1
        for i in range(n-1):
            p_sum=sum
            sum=fib
            fib=p_sum+sum
        return fib
