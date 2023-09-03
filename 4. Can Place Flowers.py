class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        a = 0    
        for i in range(len(flowerbed)):
            if i==0 and flowerbed[i] == 0:
                if len(flowerbed) == 1:
                    a += 1
                    flowerbed[i] = 1
                elif len(flowerbed) > 1 and flowerbed[i+1] == 0:
                    a += 1
                    flowerbed[i] = 1
                continue
            elif i==len(flowerbed)-1:
                if flowerbed[i-1] == 0 and flowerbed[i] == 0:
                    a += 1
                    flowerbed[i] = 1
            elif flowerbed[i-1] == 0 and \
                    flowerbed[i+1] == 0 and \
                    flowerbed[i] == 0:
                a += 1
                flowerbed[i] = 1

        return True if a >= n else False
