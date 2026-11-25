"""
Longest Check-in Streak with Gap k — given UNLABELED as the S7b +7d variant of LC 128 (25 Nov 2026), solved cold.

A gym logs the days a member checked in (unsorted, may contain duplicates).
Given k, return the length of the longest streak where each check-in is exactly k days after the previous one.

[10, 4, 20, 7, 1, 13, 4, 16], k=3 → 6 (1 → 4 → 7 → 10 → 13 → 16)

Why sorting + adjacent gaps FAILS: chains interleave. [1, 2, 4, 5, 7], k=3 → sorted gaps 1,2,1,2 → 1,
but the real answer is 3 (1 → 4 → 7).

Pattern (same as LC 128 / 2501): put everything in a set, only START a walk at a chain start
(x - k not in the set), then walk x → x + k while in the set.
Time O(n): every number is walked at most once in total (one chain, walked only from its start).
Space O(n) for the set.
Slips: coded before saying approach + complexity (2nd time); first version returned 1 for [] → init 0.
Open edge: k = 0 → no element is a chain start (x - 0 is always in the set) → returns 0; clarify with interviewer.
"""


def find_longest_streak_with_gap(arr, gap):
    set_arr = set(arr)
    l_streak = 0
    for i in set_arr:
        if i - gap not in set_arr:  # chain start
            cur_num = i
            streak = 1
            while cur_num + gap in set_arr:
                streak += 1
                cur_num += gap
            l_streak = max(l_streak, streak)
    return l_streak


if __name__ == "__main__":
    assert find_longest_streak_with_gap([10, 4, 20, 7, 1, 13, 4, 16], 3) == 6
    assert find_longest_streak_with_gap([1, 2, 4, 5, 7], 3) == 3
    assert find_longest_streak_with_gap([], 3) == 0
    assert find_longest_streak_with_gap([5], 3) == 1
    assert find_longest_streak_with_gap([1, 1, 1], 2) == 1
    print("all tests passed")
