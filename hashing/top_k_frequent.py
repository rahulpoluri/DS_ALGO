"""
    Top K Frequent Elements (LeetCode 347)

Given a list of integers nums and an integer k, return the k most frequent elements, in any order.

nums = [1, 1, 1, 2, 2, 3], k = 2 → [1, 2]
nums = [1], k = 1 → [1]
nums = [4, 4, 5, 5, 5, 6], k = 1 → [5]

You can assume the answer is unique. This is a two-pass problem: count first, then pick.


"""
from collections import Counter

def k_frequent_elements(array, k):
    elem_count = Counter(array)
    final = sorted(elem_count.items(), key= lambda x : x[1], reverse=True)[:k]
    return [key for key, value in final]

# print(k_frequent_elements([1, 1, 1, 2, 2, 3], 2))


if __name__ == "__main__":
    assert sorted(k_frequent_elements([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert k_frequent_elements([1], 1) == [1]
    assert k_frequent_elements([4, 4, 5, 5, 5, 6], 1) == [5]
    print("all tests passed")
