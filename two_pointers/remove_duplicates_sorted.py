"""
Remove Duplicates from Sorted Array (LeetCode 26)

Given a list nums sorted in ascending order, remove the duplicates in place so each value appears only once, keeping the original order. Return k, the number of unique values. The first k positions of nums must hold those unique values; what’s left after them doesn’t matter.

[1, 1, 2] → returns 2, and nums starts with [1, 2, ...]
[0, 0, 1, 1, 1, 2, 2, 3, 3, 4] → returns 5, and nums starts with [0, 1, 2, 3, 4, ...]
[1] → returns 1

Do it in O(1) extra space.

"""
 # ok, its like if you dont find same number write next to it the new one and not on it
def move_uniques_in_start(arr):
    slow = 0
    for fast in range(1,len(arr)):
        if arr[fast] != arr[slow]:
            slow+=1
            arr[slow]=arr[fast]
            

    return arr, slow+1

# print(move_uniques_in_start([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))


if __name__ == "__main__":
    arr, k = move_uniques_in_start([1, 1, 2]); assert k == 2 and arr[:k] == [1, 2]
    arr, k = move_uniques_in_start([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]); assert k == 5 and arr[:k] == [0, 1, 2, 3, 4]
    arr, k = move_uniques_in_start([1]); assert k == 1
    print("all tests passed")
