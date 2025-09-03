class Solution:
    def swapBits(self, n):
        even_bits = (n & 0xAAAAAAAA) >> 1  
        odd_bits = (n & 0x55555555) << 1  
        return even_bits | odd_bits
