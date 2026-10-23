class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[]
        count=0
        m=0
        for ch in s:
            if ch in '(':
                stack.append(ch)
                count+=1
                m=max(m,count)
            elif ch in ')':
                if stack:
                    stack.pop()
                    count-=1
        return m

              
        
