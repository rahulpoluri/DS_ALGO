# Algo Cheat Sheet — trigger → pattern → template

## Stack (matching / nesting)
**Triggers:** brackets, open/close, ENTER/EXIT, start/end, "valid order", "most recent first", nested.

**Recipe (Rahul's words, 9 Nov 2026):**
1. One stack — or one stack PER KEY (`defaultdict(list)`) depending on problem (Certivity: per worker).
2. Opposites dict: closer → opener.
3. Loop: opener → append · closer → stack empty OR top doesn't match → `return False`, else pop.
4. End: `return not stack` (leftovers = unclosed).

```python
def is_valid(s):
    stack = []
    match = {")": "(", "]": "[", "}": "{"}
    for ch in s:
        if ch not in match:
            stack.append(ch)
        elif not stack or stack.pop() != match[ch]:
            return False
    return not stack
```
**Traps:** empty stack before peek (`")"`) · mismatch must FAIL NOW, don't patch · test `""`, `"("`, `")"`, `"(])"`.
**Same pattern:** LC 20 Valid Parentheses · LC 636 Exclusive Time of Functions · Certivity worker-logs.

## Monotonic stack (next greater / next warmer)
**Triggers:** "next greater/warmer/higher", "how many days until", "nearest bigger to the right", O(n²) too slow.

**Recipe:** stack holds INDICES of items still waiting. Each item, same 2 steps, no special cases:
1. `while` stack and current beats the top → pop, record answer (`i - j`).
2. Push current index.
Leftovers never found one → default `0` (pre-fill output).

```python
def daily_temperatures(arr):
    output = [0] * len(arr)
    stack = []
    for i in range(len(arr)):
        while stack and arr[i] > arr[stack[-1]]:
            j = stack.pop()
            output[j] = i - j
        stack.append(i)
    return output
```
**Traps:** push INDEX not value · `while` not `if` (one day releases many) · output by index, not `append` ·
test EQUAL values (`[50, 50, 60]`) · O(n): each index pushed + popped once.
**Same pattern:** LC 739 Daily Temperatures · LC 496/503 Next Greater Element · LC 901 Stock Span · LC 84 Largest Rectangle.

## Hashset — run start (consecutive sequences)
**Triggers:** "consecutive", "longest run/streak", unsorted input, "must be O(n)" (= sorting is banned).

**Recipe:** set for O(1) "does x exist?". Only start counting where a run BEGINS (`x - 1 not in s`), walk up.
```python
def longest_consecutive(nums):
    s = set(nums)
    best = 0
    for x in s:                     # loop the set (dupes gone)
        if x - 1 not in s:          # run start only
            length = 1
            while x + length in s:
                length += 1
            best = max(best, length)
    return best
```
**Traps:** walking from EVERY number = O(n²) · counting "has a neighbour" ≠ run length · loop `arr` with dupes = repeat work ·
test `[]`, `[5,5]`, two separate runs `[1,2,10,11,12]` · O(n): each number walked once (amortized, like monotonic stack).
**Same pattern:** LC 128 Longest Consecutive Sequence · LC 1, 217 (set/dict lookup family).

## Sliding window (variable size)
**When:** longest/shortest CONSECUTIVE run (subarray/substring) meeting a condition, values that only grow the sum (positives).
**Why O(n):** right moves n times, left moves at most n times. Left never goes back: with positives, if [l..r] is
over budget, every longer window starting at l is too.
```python
left = cur = best = 0
for right, x in enumerate(arr):
    cur += x                       # 1. add
    while cur > budget:            # 2. shrink until valid
        cur -= arr[left]; left += 1
    best = max(best, right - left + 1)   # 3. record (always valid here)
```
**Variant:** `if` instead of `while` = non-shrinking window (length always = best so far; also correct for "longest").
**Traps:** recording a window before it's valid · missing the last window (record after adding) · `<` vs `<=` ·
negatives break it (use prefix sums) · test exact-budget, one huge value, `[]`.
**Same pattern:** LC 209 Min Size Subarray Sum · LC 1004 Max Consecutive Ones III · LC 3 Longest Substring w/o Repeat · LC 904.
