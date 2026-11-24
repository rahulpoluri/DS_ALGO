"""
Longest Run of Days Under Budget (variable sliding window; same shape as LeetCode 1004 / 209 / 904)

You get daily spending (all positive) and a budget. Return the length of the longest run of
CONSECUTIVE days whose total spend is <= budget.

[20, 50, 10, 30, 40, 10, 10, 60], budget 70 → 3  ([40, 10, 10] = 60)
[10, 100, 10], 20 → 1
[10, 10], 50 → 2
[20, 50], 70 → 2   (exactly the budget counts)

Naive: try every start, extend → O(n²). Aim for O(n).
"""

# My path (24 Nov 2026, evening, "for fun"):
# - Approach named right away: "move like a snail — add at the front, remove from the left end".
# - Attempt 1: if/else stepping one pointer at a time, recorded the length in the else branch
#   → recorded an OVER-budget window ([50, 10, 30] = 90); right answer 3 only by luck. Broke on [10, 100, 10], 20.
# - Attempt 2: recorded BEFORE adding → last window never checked + used < instead of <=.
# - Attempt 3 (below): for-loop + add → check → if over, drop ONE from the left (if, not while).
#   Correct! This is the "non-shrinking window": the window length always equals the best found so far;
#   when over budget it slides (add 1, drop 1) instead of shrinking, and it only grows when a longer valid window exists.
# Lesson: record a window only when you KNOW it's valid; test edge inputs (exact budget, last window, one huge value).
# Open: never answered WHY left may only move forward (answer: all values positive → if [l..r] is over budget,
#   every window [l..r'] with r' > r is too, so l is never needed again).


def find_longest_days_under_budget(spend_arr, budget):
    """Rahul's version — non-shrinking window (if instead of while)."""
    max_days = 0
    back_ind = 0
    cur_sum = 0
    for front_ind in range(len(spend_arr)):
        cur_sum += spend_arr[front_ind]
        if cur_sum <= budget:
            max_days = max(max_days, front_ind - back_ind + 1)
        else:
            cur_sum -= spend_arr[back_ind]
            back_ind += 1
    return max_days


def longest_under_budget_classic(spend, budget):
    """Standard shrinking window: add → shrink WHILE over → record (always valid)."""
    left = cur = best = 0
    for right, x in enumerate(spend):
        cur += x
        while cur > budget:
            cur -= spend[left]
            left += 1
        best = max(best, right - left + 1)
    return best


if __name__ == "__main__":
    cases = [
        (([20, 50, 10, 30, 40, 10, 10, 60], 70), 3),
        (([10, 100, 10], 20), 1),
        (([10, 10], 50), 2),
        (([20, 50], 70), 2),
        (([100], 50), 0),
        (([], 10), 0),
    ]
    for fn in (find_longest_days_under_budget, longest_under_budget_classic):
        for (arr, b), want in cases:
            got = fn(arr, b)
            assert got == want, (fn.__name__, arr, b, got, want)
    import random
    for _ in range(2000):
        arr = [random.randint(1, 50) for _ in range(random.randint(0, 12))]
        b = random.randint(0, 120)
        assert find_longest_days_under_budget(arr, b) == longest_under_budget_classic(arr, b)
    print("all tests passed")
