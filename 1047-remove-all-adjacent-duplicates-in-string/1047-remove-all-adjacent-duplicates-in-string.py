class Solution:
    def removeDuplicates(self, S: str) -> str:
        stk = []
        for ch in S:
            if stk and stk[-1] == ch:
                stk.pop()
            else:
                stk.append(ch)
        return "".join(stk)