class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip().split()
        s = reversed(s)
        return " ".join(s)
            