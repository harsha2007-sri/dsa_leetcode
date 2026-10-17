class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        first = nums[:n]
        second = nums[n:]
        final=[]
        for i in range(n):
            final.append(first[i])
            final.append(second[i])
        return final
