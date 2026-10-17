class Solution:
    def minSubArrayLen(self, target: int, l: List[int]) -> int:
        left=0
        right=0
        s=0
        min_len=float('inf')
        while right<len(l):
            s+=l[right]
            while s>=target:
                length=right-left+1
                min_len=length if length<min_len else min_len
                s-=l[left]
                left+=1
            right+=1
        if min_len==float('inf'):
            return 0
        else:
            return min_len
