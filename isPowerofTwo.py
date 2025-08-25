import math
class Solution:
    def isPowerofTwo(self, n):
        if n <= 0:
            return False
        log = math.log2(n)
        return log.is_integer()
