"""
Valid Parentheses (LeetCode 20)

Given a string s containing only ( ) { } [ ], return True if every opening bracket is closed
by the same type, in the correct order, and every closing bracket has a matching opener.

"()" → True · "()[]{}" → True · "(]" → False · "([)]" → False · "{[]}" → True
"""

# My solution (9 Nov 2026, ~11 min + 1 fix): a mismatched closer is pushed and can never be
# popped, so it "poisons" the stack → final False. Works, but the template below is clearer.
def check_valid_parenthesis(arr):
    stack = []
    opposites = {")": "(", "]": "[", "}": "{"}
    for i in arr:
        if not stack:
            stack.append(i)
        elif i not in opposites:
            stack.append(i)
        elif stack[-1] == opposites[i]:
            stack.pop(-1)
        else:
            stack.append(i)

    if stack:
        return False
    return True


# Template version (see cheatsheet.md → Stack): closer must match top, else FAIL NOW.
def is_valid(s):
    stack = []
    match = {")": "(", "]": "[", "}": "{"}
    for ch in s:
        if ch not in match:
            stack.append(ch)
        elif not stack or stack.pop() != match[ch]:
            return False
    return not stack


if __name__ == "__main__":
    cases = {"()": True, "()[]{}": True, "(]": False, "([)]": False, "{[]}": True,
             "": True, "(": False, ")": False, "((": False, "(])": False}
    for fn in (check_valid_parenthesis, is_valid):
        for s, want in cases.items():
            assert fn(s) is want, (fn.__name__, s)
    print("all tests passed")
