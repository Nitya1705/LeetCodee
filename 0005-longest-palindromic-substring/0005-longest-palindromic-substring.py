class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Finds the longest palindromic substring in the given string 's'.
        Time Complexity: O(n²)
        Space Complexity: O(1)
        """
        if not s or len(s) < 1:
            return ""
        
        start, end = 0, 0
        
        def expand_around_center(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        for i in range(len(s)):
            # Case 1: Odd-length palindromes (e.g., "aba" centered at 'b')
            len1 = expand_around_center(i, i)
            
            # Case 2: Even-length palindromes (e.g., "cbbd" centered between 'b' and 'b')
            len2 = expand_around_center(i, i + 1)
            
            # Get the maximum length found at the current index
            max_len = max(len1, len2)
            
            # If the new palindrome is longer than our previous best, update our boundaries
            if max_len > (end - start):
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
                
        return s[start : end + 1]


# Driver code to run and test the solution
if __name__ == "__main__":
    solver = Solution()
    
    # Test Case 1
    input_1 = "babad"
    print(f"Input: '{input_1}' -> Longest Palindrome: '{solver.longestPalindrome(input_1)}'")
    # Output: "bab" or "aba" are both valid answers
    
    # Test Case 2
    input_2 = "cbbd"
    print(f"Input: '{input_2}' -> Longest Palindrome: '{solver.longestPalindrome(input_2)}'")
    # Output: "bb"
