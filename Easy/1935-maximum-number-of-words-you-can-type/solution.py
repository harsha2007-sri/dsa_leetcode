class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        count = 0
        words = text.split()
        for word in words:
            flag = True
            for ch in brokenLetters:
                if ch in word:
                    flag = False
                    break
            if flag:
                count += 1
        return count
