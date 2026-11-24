"""
Daily Temperatures (LeetCode 739)

Given daily temperatures, return for each day how many days until a WARMER temperature.
If no warmer day ever comes, put 0. Up to 100,000 days → O(n^2) nested loops too slow.

[73, 74, 75, 71, 69, 72, 76, 73] → [1, 1, 4, 2, 1, 1, 0, 0]
"""

# My path (11 Nov 2026, ~1.5 h with hints):
# - 1st idea: dict temp→index, look up "next higher number" → WRONG: the nearest warmer day is ANY warmer
#   temp that comes first ([75, 80, 76]: answer for 75 is 1 via 80, not 2 via 76).
# - Hint "keep the days still waiting" → I named it: waiting days go on a stack, released by a warmer day.
# - Coded it with if/elif cases (neighbour checks, manual ind += 1) → 3 rounds of patching:
#   appended output in release order, last day never processed, EQUAL temps → infinite loop.
# Lesson: every day does the SAME two steps, no special cases. Patching cases = over-engineering.
# 15 Nov 2026: COLD redo ✅ ~7 min, named the pattern. Gap: complexity — said "O(n+k)"; it's amortized O(n)
#   (each index pushed once, popped at most once → ≤ n pops in total). Space O(n) (decreasing input).

# Template (see cheatsheet.md → Monotonic stack)
def daily_temperatures(arr):
    output = [0] * len(arr)
    stack = []                                   # indices of days still waiting (temps decreasing)
    for i in range(len(arr)):
        while stack and arr[i] > arr[stack[-1]]: # today releases every colder waiting day
            j = stack.pop()
            output[j] = i - j
        stack.append(i)                          # today waits too
    return output


if __name__ == "__main__":
    cases = [
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
        ([30, 40, 50, 60], [1, 1, 1, 0]),
        ([70, 60, 80], [2, 1, 0]),
        ([75, 80, 76], [1, 0, 0]),
        ([50, 50, 60], [2, 1, 0]),          # equal temps (my version hung here)
        ([60, 50, 50, 70], [3, 2, 1, 0]),
        ([90, 80, 70], [0, 0, 0]),
        ([], []),
        ([42], [0]),
    ]
    for arr, want in cases:
        assert daily_temperatures(arr) == want, (arr, daily_temperatures(arr))
    print("all tests passed")

# Re-solve 24 Nov 2026 (re-skinned as "days until a higher account balance", for fun, evening):
# - Naive O(n^2) named right, but claimed "less than O(n^2) because the list shrinks" -> wrong, n + (n-1) + ... = O(n^2).
# - Recognised the monotonic stack from 901 after 1 hint; coded it correctly first try (indices + values on stack,
#   answer written to the POPPED day, strict >). Output [2, 1, 3, 2, 1, 0, 0] correct.
