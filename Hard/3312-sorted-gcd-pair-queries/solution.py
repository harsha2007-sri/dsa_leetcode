from bisect import bisect_left
class Solution(object):
    def gcdValues(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        max_num = max(nums)

        freq = [0] * (max_num + 1)
        for num in nums:
            freq[num] += 1

        gcd_count = [0] * (max_num + 1)

        for g in range(max_num, 0, -1):
            count = 0

            for multiple in range(g, max_num + 1, g):
                count += freq[multiple]

            pairs = count * (count - 1) // 2

            for multiple in range(2 * g, max_num + 1, g):
                pairs -= gcd_count[multiple]

            gcd_count[g] = pairs

        prefix = [0] * (max_num + 1)
        for i in range(1, max_num + 1):
            prefix[i] = prefix[i - 1] + gcd_count[i]

        ans = []
        for q in queries:
            ans.append(bisect_left(prefix, q + 1))

        return ans
