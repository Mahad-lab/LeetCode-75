class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result = []
        greatest = max(candies)
        for kidCandy in candies:
            if kidCandy+extraCandies >= greatest:
                result.append(True)
            else:
                result.append(False)
        return result
        
