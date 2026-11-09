"""
Valid Anagram (LeetCode 242)

Given two strings s and t, return True if t is an anagram of s, and False otherwise. An anagram uses exactly the same letters, each the same number of times, in any order.

s = "anagram", t = "nagaram" → True
s = "rat", t = "car" → False
s = "listen", t = "silent" → True
s = "aab", t = "ab" → False
"""
from collections import Counter

def if_anagram(s1, s2):
    hash_map1 = {}
    hash_map2 = {}

    for i in s1:
        hash_map1[i]  = hash_map1.get(i,0) + 1
    for i in s2:
        hash_map2[i]  = hash_map2.get(i, 0) + 1

    return hash_map2 == hash_map1

# print(if_anagram("anagram", "nagaram"))
# print(Counter("anagram") == Counter("nagaram"))
# # print(if_anagram("rat", "car"))
# print(Counter("rat") == Counter("car"))
# # print(if_anagram("aab", "ab"))
# print(Counter("aab") == Counter("ab"))


if __name__ == "__main__":
    assert if_anagram("anagram", "nagaram") is True
    assert if_anagram("rat", "car") is False
    assert if_anagram("listen", "silent") is True
    assert if_anagram("aab", "ab") is False
    print("all tests passed")
