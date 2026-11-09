"""
Contains Duplicate (LeetCode 217)

You’re given a list of integers nums. Return True if any value appears at least twice, and False if every value is distinct.

[1, 2, 3, 1] → True
[1, 2, 3, 4] → False
[1, 1, 1, 3, 3, 4, 3, 2, 4, 2] → True

"""
# a = [1, 2, 3, 1]
# b = [1, 2, 3, 4]
# c = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

def find_if_duplicate(array):
    hash_set = set()
    for value in array:
        if value in hash_set:
            return True
        hash_set.add(value)
    return False

# print(find_if_duplicate(a))
# print(find_if_duplicate(b))
# print(find_if_duplicate(c))


if __name__ == "__main__":
    assert find_if_duplicate([1, 2, 3, 1]) is True
    assert find_if_duplicate([1, 2, 3, 4]) is False
    assert find_if_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
    assert find_if_duplicate([]) is False
    print("all tests passed")
