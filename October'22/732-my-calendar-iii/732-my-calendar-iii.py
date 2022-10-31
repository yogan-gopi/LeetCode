from sortedcontainers import SortedList
class MyCalendarThree:

    def __init__(self):
        self.max = 0
        self.prev = SortedList()

    def book(self, start: int, end: int) -> int:
        self.prev.add((start, 1))
        self.prev.add((end, -1))
        
        count = 0
        for i, j in self.prev:
            count += j
            self.max = max(self.max, count)
        return self.max


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)