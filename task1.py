class Solution(object):
    def isHappy(self, n):
        while n >= 1:
            i = n
            n = 0
            while i > 0:
                n += (i % 10) ** 2
                i = i // 10
            if n == 1:
                return True
            if n == 4:
                return False