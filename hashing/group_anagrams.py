"""
Group Anagrams (LeetCode 49)

Given a list of strings strs, group the anagrams together. You can return the groups in any order.

["eat", "tea", "tan", "ate", "nat", "bat"] → [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
[""] → [[""]]
["a"] → [["a"]]

All strings are lowercase English letters.

"""

def group_anagrams(array):
    hash_map = dict()
    for s in array:
        sorted_s = "".join(sorted(s))
        if sorted_s in hash_map:
            hash_map[sorted_s].append(s)
        else:
            hash_map[sorted_s] = [s]
            

    return list(hash_map.values())

# print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


if __name__ == "__main__":
    norm = lambda groups: sorted(sorted(g) for g in groups)
    assert norm(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) == norm([["eat", "tea", "ate"], ["tan", "nat"], ["bat"]])
    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]
    print("all tests passed")
