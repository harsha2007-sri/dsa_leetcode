class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        c0 = c1 = c2 = 0
        for x in nums:
            if x == 0:
                c0 += 1
            elif x == 1:
                c1 += 1
            else:
                c2 += 1
        i = 0
        while c0 > 0:
            nums[i] = 0
            i += 1
            c0 -= 1
        while c1 > 0:
            nums[i] = 1
            i += 1
            c1 -= 1
        while c2 > 0:
            nums[i] = 2
            i += 1
            c2 -= 1
