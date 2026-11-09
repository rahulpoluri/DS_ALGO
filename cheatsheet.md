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
