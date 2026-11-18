"""
Longest Square Streak in an Array (LeetCode 2501) — given UNLABELED as the +3d variant of LC 128 (18 Nov 2026), solved cold ~17 min.

You're given an array of integers nums. A streak is a subsequence of length at least 2 where, after sorting,
every element except the first is the square of the element before it.
Return the length of the longest streak, or -1 if none exists.

[4, 3, 6, 16, 8, 2] → 3 (2 → 4 → 16)
[2, 3, 5, 6, 7] → -1
Constraints: 2 ≤ len ≤ 10^5, 2 ≤ nums[i] ≤ 10^5

Pattern (same as LC 128): put everything in a set, only START a walk at a chain start
(sqrt(x) not in the set), then walk x → x*x while in the set.
Time O(n): every number is walked at most once in total (it belongs to one chain, walked only from its start).
Space O(n) for the set. Chains are tiny here anyway (2 → 4 → 16 → 256 → 65536).
"""
import math


def return_longest_streak_len(arr):
    s_arr = set(arr)
    l_len = 1
    for i in s_arr:
        r = math.isqrt(i)
        if not (r * r == i and r in s_arr):  # i is a chain start
            j = i
            cur_len = 1
            while j * j in s_arr:
                cur_len += 1
                j = j * j
            l_len = max(l_len, cur_len)
    return -1 if l_len == 1 else l_len


if __name__ == "__main__":
    assert return_longest_streak_len([4, 3, 6, 16, 8, 2]) == 3
    assert return_longest_streak_len([2, 3, 5, 6, 7]) == -1
    assert return_longest_streak_len([2, 4]) == 2
    assert return_longest_streak_len([2, 4, 16, 256, 65536]) == 5
    assert return_longest_streak_len([4, 16, 2, 2, 4]) == 3
    assert return_longest_streak_len([3, 9, 81, 5, 25]) == 3
    print("all tests passed")
