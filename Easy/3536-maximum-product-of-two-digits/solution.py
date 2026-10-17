class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = b = 0

        while n > 0:
            x = n % 10
            n //= 10

            if x > a:
                b = a
                a = x
            elif x > b:
                b = x

        return a * b
