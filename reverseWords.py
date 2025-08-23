class Solution:
    def reverseWords(self, s):
        words = [w for w in s.split(".") if w]   # filter out empty words
        return ".".join(words[::-1])
