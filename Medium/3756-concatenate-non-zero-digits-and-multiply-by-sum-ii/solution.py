class Solution(object):
    def sumAndMultiply(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10**9 + 7
        pos = []
        dig = []
        for i, ch in enumerate(s):
            if ch != '0':
                pos.append(i)
                dig.append(int(ch))
        m = len(dig)
        pow10 = [1] * (m + 1)
        pre = [0] * (m + 1)
        preSum = [0] * (m + 1)
        for i in range(m):
            pow10[i + 1] = (pow10[i] * 10) % MOD
            pre[i + 1] = (pre[i] * 10 + dig[i]) % MOD
            preSum[i + 1] = preSum[i] + dig[i]
        first = [m] * (len(s) + 1)
        last = [-1] * len(s)
        j = 0
        for i in range(len(s)):
            while j < m and pos[j] < i:
                j += 1
            first[i] = j
        j = m - 1
        for i in range(len(s) - 1, -1, -1):
            while j >= 0 and pos[j] > i:
                j -= 1
            last[i] = j

        ans = []

        for l, r in queries:
            L = first[l]
            R = last[r]

            if L > R:
                ans.append(0)
                continue

            length = R - L + 1
            x = (pre[R + 1] - pre[L] * pow10[length]) % MOD
            sm = preSum[R + 1] - preSum[L]
            ans.append((x * sm) % MOD)

        return ans
        
