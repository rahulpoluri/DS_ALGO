"""
Contains Duplicate II (LeetCode 219)

Given a list nums and an integer k, return True if there are two different positions i and j where nums[i] == nums[j] and the distance between them is at most k (abs(i - j) <= k).

nums = [1, 2, 3, 1], k = 3 → True (the two 1s are 3 apart)
nums = [1, 0, 1, 1], k = 1 → True (the last two 1s are 1 apart)
nums = [1, 2, 3, 1, 2, 3], k = 2 → False (each pair is 3 apart)
"""

def find_duplicates_at_distance(arr, k):
    hash_map = dict()
    for ind, val in enumerate(arr):
        if val in hash_map and abs(hash_map[val] - ind) <= k:
            return True
        hash_map[val] = ind
    return False


if __name__ == "__main__":
    assert find_duplicates_at_distance([1, 2, 3, 1], 3) is True
    assert find_duplicates_at_distance([1, 0, 1, 1], 1) is True
    assert find_duplicates_at_distance([1, 2, 3, 1, 2, 3], 2) is False
    print("all tests passed")
