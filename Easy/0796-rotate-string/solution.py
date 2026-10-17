class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        l=len(s)
        flag=False
        for i in range(l):
            if s == goal:
                flag=True
            ls=s[0]
            s=s[1:]+ls
        return flag
