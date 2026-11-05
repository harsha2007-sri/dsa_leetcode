class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        """sum=1
        p_sum=0
        fib=1
        for i in range(n-1):
            p_sum=sum
            sum=fib
            fib=p_sum+sum
        return fib"""
        dp=[]
        for i in range(n+1):
            dp.insert(i,-1)
        return self.calculate(n,dp)
    def calculate(self,n,dp):
        if n<0:
            return 0
        if n==0:
            return 1
        if dp[n]!=-1:
            return dp[n]
        dp[n]=self.calculate(n-1,dp)+self.calculate(n-2,dp)
        return dp[n]
