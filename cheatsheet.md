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
