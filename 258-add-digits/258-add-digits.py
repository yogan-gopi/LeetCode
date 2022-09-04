class Solution:
    def addDigits(self, num: int) -> int:
        def add(n):
            sum = 0
            while n > 0:
                sum += (n%10)
                n//=10
            return sum
        if num == 0:
            return num
        while num > 9:
            num = add(num)
        return num