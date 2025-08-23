#User function Template for python3

class Solution:
    # Function to find uncommon characters between two strings.
    def uncommonChars(self, s1, s2):
        unsorted = ''
        for char in s1:
            if char not in s2:
                  unsorted = unsorted+char
        for char in s2:
            if char not in s1:
                  unsorted = unsorted+char
        sorted_char = sorted(set(unsorted))
        return "".join(sorted_char)
