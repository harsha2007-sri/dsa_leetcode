class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return "0"
        
        ans = ""
        if (numerator < 0) != (denominator < 0):
            ans += "-"
        numerator = abs(numerator)
        denominator = abs(denominator)
        ans += str(numerator // denominator)
        r = numerator % denominator
        if r == 0:
            return ans
        else:
            ans += "."
            seen = {}
            while r:
                if r in seen:
                    i = seen[r]
                    ans = ans[:i] + "(" + ans[i:] + ")"
                    break
                seen[r] = len(ans)
                r *= 10
                ans += str(r // denominator)
                r %= denominator
            return ans
            
