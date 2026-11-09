"""
Squares of a Sorted Array (LeetCode 977)

Given a list nums sorted in ascending order, which can contain negative numbers, return a new list of the squares of each number, also sorted in ascending order.

[-4, -1, 0, 3, 10] → [0, 1, 9, 16, 100]
[-7, -3, 2, 3, 11] → [4, 9, 9, 49, 121]
[1, 2, 3] → [1, 4, 9]

The easy way is to square everything and sort, which is O(n log n). Aim for O(n).

Hint for thinking: in [-4, -1, 0, 3, 10], where are the biggest squares?
"""

def sorted_squares(arr):
    left, right = 0, len(arr)-1
    final_list = []
    while left <= right:
        if arr[left]*arr[left]> arr[right] * arr[right]:
            final_list.append(arr[left]*arr[left])
            left+=1
        else:
            final_list.append(arr[right]*arr[right])
            right -=1

    return final_list[::-1]

# print(sorted_squares([-4, -1, 0, 3, 10]))


if __name__ == "__main__":
    assert sorted_squares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
    assert sorted_squares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]
    assert sorted_squares([1, 2, 3]) == [1, 4, 9]
    print("all tests passed")
