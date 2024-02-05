class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = ""
        for i in range(len(s)):
            current_substring = ""
            for j in range(i, len(s)):
                if s[j] in current_substring:
                    break 
                else:
                    current_substring = current_substring + s[j]
            if len(current_substring) > len(longest_substring):
                longest_substring = current_substring
        return len(longest_substring)