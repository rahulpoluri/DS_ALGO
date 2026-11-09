"""
First Unique Character in a String (LeetCode 387)

Given a string s, return the index of the first character that appears only once. If there isn’t one, return -1.

"leetcode" → 0 (the l appears once)
"loveleetcode" → 2 (the v)
"aabb" → -1

All letters are lowercase.
"""
from collections import Counter

def return_index_of_only_letter(s):
    count_map = Counter(s)
    for ind, char in enumerate(s):
        if count_map[char] == 1:
            return ind
    return -1

# print(return_index_of_only_letter("loveleetcode"))


if __name__ == "__main__":
    assert return_index_of_only_letter("leetcode") == 0
    assert return_index_of_only_letter("loveleetcode") == 2
    assert return_index_of_only_letter("aabb") == -1
    assert return_index_of_only_letter("") == -1
    print("all tests passed")
