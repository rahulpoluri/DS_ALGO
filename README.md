# DS & Algo practice — pattern-first

Goal: recognise the pattern in the first 2 minutes, then write its template from memory.
Every file = problem statement + my solution + tests. Run any file: `python3 two_pointers/move_zeroes.py`

Templates & triggers: [cheatsheet.md](cheatsheet.md)

| # | Problem | LC | Pattern | Date | Status |
|---|---------|----|---------|------|--------|
| 1 | [Contains Duplicate](hashing/contains_duplicate.py) | 217 | Hashing | 2026-11-07/08 | ✅ |
| 2 | [Valid Anagram](hashing/valid_anagram.py) | 242 | Hashing | 2026-11-07/08 | ✅ (fixed 9 Nov: assign the count back) |
| 3 | [Group Anagrams](hashing/group_anagrams.py) | 49 | Hashing | 2026-11-07/08 | ✅ |
| 4 | [Top K Frequent Elements](hashing/top_k_frequent.py) | 347 | Hashing | 2026-11-07/08 | ✅ |
| 5 | [First Unique Character](hashing/first_unique_char.py) | 387 | Hashing | 2026-11-07/08 | ✅ |
| 6 | [Contains Duplicate II](hashing/contains_duplicate_ii.py) | 219 | Hashing | 2026-11-07/08 | ✅ |
| 7 | [Valid Palindrome](two_pointers/valid_palindrome.py) | 125 | Two pointers (opposite ends) | 2026-11-07/08 | ✅ |
| 8 | [Two Sum II](two_pointers/two_sum_ii.py) | 167 | Two pointers (opposite ends) | 2026-11-07/08 | ✅ |
| 9 | [Move Zeroes](two_pointers/move_zeroes.py) | 283 | Two pointers (slow/fast) | 2026-11-07/08 | ✅ |
| 10 | [Remove Duplicates from Sorted Array](two_pointers/remove_duplicates_sorted.py) | 26 | Two pointers (slow/fast) | 2026-11-07/08 | ✅ |
| 11 | [Squares of a Sorted Array](two_pointers/squares_sorted_array.py) | 977 | Two pointers (opposite ends) | 2026-11-07/08 | ✅ |
| 12 | [Container With Most Water](two_pointers/container_most_water.py) | 11 | Two pointers (opposite ends) | 2026-11-07/08 | ✅ |
| 13 | [Valid Parentheses](stack/valid_parentheses.py) | 20 | Stack | 2026-11-09 | ✅ |
| 14 | [Daily Temperatures](stack/daily_temperatures.py) | 739 | Monotonic stack | 2026-11-11 | ✅ with hints (patched cases 3× → redo cold) · ✅ COLD 15 Nov (~7 min) |
| 15 | [Longest Consecutive Sequence](hashing/longest_consecutive_sequence.py) | 128 | Hashset (run start) | 2026-11-15 | ❌→✅ cold fail (O(n²)), fixed with hint |
| 16 | [Longest Square Streak](hashing/longest_square_streak.py) | 2501 | Hashset (run start) — unseen variant of 128 | 2026-11-18 | ✅ COLD ~17 min, pattern transferred |
| 17 | [Online Stock Span](stack/online_stock_span.py) | 901 | Monotonic stack — unseen variant of 739 | 2026-11-23 | ✅ with 2 hints (stuck 32 min; class-attr bug fixed) |
