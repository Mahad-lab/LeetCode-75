class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        
        word3 = ""
        lw1, lw2 = len(word1), len(word2)
        for i in range(max(lw1, lw2)):
            if i < lw1:
                word3 = word3 + word1[i]
            if i < lw2:
                word3 = word3 + word2[i]
        return word3
