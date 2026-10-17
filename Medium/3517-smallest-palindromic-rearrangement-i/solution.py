class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        left = list(s[:n // 2])
        left.sort()
        ans = "".join(left)
        if n % 2 == 1:
            return ans + s[n // 2] + ans[::-1]
        return ans + ans[::-1]
