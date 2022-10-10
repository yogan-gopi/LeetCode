class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n < 2:
            return ""
        
        for i in range(n//2):
            if palindrome[i] != "a":
                palindrome = palindrome.replace(palindrome[i], "a", 1)
                return palindrome
        
        text = list(palindrome)
        text[-1] = "b"
        return "".join(text)