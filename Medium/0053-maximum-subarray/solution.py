class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = nums[0]
        max_sum = nums[0]

        for i in range(1,len(nums)):
            s = cur + nums[i]
            if s > nums[i]:
                cur = cur + nums[i]
            else:
                cur = nums[i]

            if cur > max_sum:
                max_sum = cur

        return max_sum
