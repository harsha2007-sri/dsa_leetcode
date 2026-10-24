class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[]
        count=0
        for char in s:
            if char=='(':
                stack.append(char)
            else:
                if stack and stack[-1]=='(':
                    stack.pop()
                else:
                    count+=1
        count+=len(stack)
        return count
            
        
