class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
                 "p", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        for i in sentence:
            if i in alpha:
                alpha.remove(i)
        if len(alpha) == 0:
            return True
        else:
            return False