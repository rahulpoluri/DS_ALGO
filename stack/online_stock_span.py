"""
Online Stock Span (LeetCode 901)

Prices arrive one per day. For each new price, return the span: how many consecutive days,
ending today and going backwards, had a price <= today's (today counts). Up to 10^4 calls,
so walking back every time (O(n) per call) is too slow in the worst case.

100, 80, 60, 70, 60, 75, 85 → 1, 1, 1, 2, 1, 4, 6
"""

# My path (23 Nov 2026, unseen variant of 739, given UNLABELED as review S4):
# - Stuck ~32 min: "without going backwards and remembering them I don't see a way".
# - Hint: when 75 swallows 60,70,60 → does 85 ever need them one by one? → I named STACK.
# - Recipe said aloud before coding: span = 1 + spans of everything popped ✅. Said "push only sometimes" ✗
#   → push ALWAYS (today represents the whole swallowed run).
# - 1st code: 3 branches (empty / lower / higher) + arr as CLASS attribute (shared by all instances = bug).
#   Fix: __init__, and the while loop alone covers all cases.
# Lessons: ask for a hint at ~15 min, not 32. Complexity again needed help → amortized O(1) per call:
#   each price pushed once, popped at most once → O(n) total. Space O(n) (falling prices).

class StockSpanner:
    def __init__(self):
        self.stack = []                              # (price, span), prices strictly decreasing

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]              # absorb the swallowed run's span
        self.stack.append((price, span))             # always push: today represents the run
        return span


if __name__ == "__main__":
    cases = [
        ([100, 80, 60, 70, 60, 75, 85], [1, 1, 1, 2, 1, 4, 6]),
        ([10, 20, 30], [1, 2, 3]),
        ([30, 20, 10], [1, 1, 1]),
        ([5, 5, 5], [1, 2, 3]),                      # equal counts (<=)
        ([42], [1]),
    ]
    for prices, want in cases:
        s = StockSpanner()                           # fresh instance per case (class-attr bug would fail here)
        got = [s.next(p) for p in prices]
        assert got == want, (prices, got)
    print("all tests passed")
