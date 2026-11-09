"""
Valid Palindrome (LeetCode 125)

Given a string s, return True if it’s a palindrome once you convert everything to lowercase and remove every character that isn’t a letter or a digit.

"A man, a plan, a canal: Panama" → True (it becomes "amanaplanacanalpanama")
"race a car" → False
" " → True (an empty string counts as a palindrome)

Try to do it without building a reversed copy of the string.
"""

def is_palindrome(s):
    # new idea just and check positions from both sides
    i, j = 0, len(s)-1
    
    while i < j:
        if not s[i].isalnum():
            i = i+1
            continue
        if not s[j].isalnum():
            j= j-1
            continue
        i1 = s[i].lower()
        j1 = s[j].lower()
        if i1 == j1:
            i = i+1
            j = j-1
            continue
        else:
            return False
    return True



# print(is_palindrome("a."))


if __name__ == "__main__":
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("race a car") is False
    assert is_palindrome(" ") is True
    assert is_palindrome("a.") is True
    print("all tests passed")
