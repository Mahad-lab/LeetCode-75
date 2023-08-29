class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        ls1, ls2 = len(str1), len(str2)
        for i in range(min(ls1, ls2), 0, -1):
            if i == 1:
                if str2[:i]*(ls2//(i)) == str2 and str1[:i]*(ls1//(i)) == str1:
                    return str1[:i]
            if ls1%(i+1) == 0 and ls2%(i+1) == 0:
                # print(str1[:i])
                if str1[:i+1]*(ls1//(i+1)) == str1 and str1[:i+1]*(ls2//(i+1)) == str2:
                    return str1[:i+1]
        return ""
