
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        best_len = 1
        best_start = 0

        def expand(L, R):
            while L >= 0 and R < n and s[L] == s[R]:
                L -= 1
                R += 1
            # after breaking, palindrome is from L+1 to R-1
            return R - L - 1, L + 1   # length, start index

        for i in range(n):
            # odd length
            len1, st1 = expand(i, i)
            if len1 > best_len:
                best_len, best_start = len1, st1

            # even length
            len2, st2 = expand(i, i + 1)
            if len2 > best_len:
                best_len, best_start = len2, st2

        return s[best_start: best_start + best_len]
