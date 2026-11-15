"""
Longest Consecutive Sequence (LeetCode 128)

Given an UNSORTED array of integers, return the length of the longest run of consecutive numbers
(1, 2, 3, 4 ...). Elements don't have to be next to each other in the array. Must run in O(n).

[100, 4, 200, 1, 3, 2]          → 4   (1, 2, 3, 4)
[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]  → 9   (0 … 8)
"""

# My path (15 Nov 2026, cold, ~35 min — FAILED in time, fixed with a hint):
# - Opened with sort + count = O(n log n) → good interview opener, but breaks the O(n) rule.
# - Try 1: dict, delete numbers with no neighbour, return len → counts EVERY number that has a
#   neighbour, not the longest run ([1, 2, 10, 11, 12] → 5, answer 3). Also KeyError on dup ([5, 5]).
# - Try 2: set + walk up from every i that has i+1 → correct but O(n²) ([1..10000] walks 9999, 9998, ...).
# - Fix (hint): only start walking at a RUN START (i-1 not in set) → each number walked once → O(n).
# Lesson: "O(n) with a while inside" = make sure each element is walked by at most ONE loop.

def longest_consecutive(arr):
    best_l = 0
    arr_s = set(arr)                  # O(1) "does x exist?" + removes duplicates
    for i in arr_s:                   # loop the SET, not arr → duplicates not repeated
        if i - 1 not in arr_s:        # i starts a run (skip if mid of a run)
            l = 1
            while i + l in arr_s:
                l += 1
            best_l = max(best_l, l)   # best length so far
    return best_l


if __name__ == "__main__":
    cases = [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([1, 2, 10, 11, 12], 3),      # my try-1 returned 5
        ([5, 5], 1),                  # my try-1 crashed (KeyError)
        ([], 0),
        ([5], 1),
        ([-2, -1, 0, 1], 4),
        ([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6], 7),
    ]
    for arr, want in cases:
        assert longest_consecutive(arr) == want, (arr, longest_consecutive(arr))
    big = list(range(100_000))
    assert longest_consecutive(big) == 100_000   # O(n²) version would crawl here
    print("all tests passed")
