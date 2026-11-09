"""
Container With Most Water (LeetCode 11)

You’re given a list height. Each number is the height of a vertical line at that position. Pick two lines that, together with the x-axis, form a container. Return the maximum amount of water it can hold.

The water in a container is width × the shorter of the two lines, where width is the distance between the two positions.

[1, 8, 6, 2, 5, 4, 8, 3, 7] → 49 (the lines at index 1 (height 8) and index 8 (height 7) give a width of 7 × min(8, 7) = 49)
[1, 1] → 1
[4, 3, 2, 1, 4] → 16

The brute force is to try every pair, which is O(n²). Aim for O(n).
"""

def give_max_area(arr):
    left, right = 0, len(arr)-1
    max_area = 0

    while left < right:
        area = min(arr[left], arr[right]) * (right - left)
        max_area = max(max_area, area)

        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1

    return max_area

# print(give_max_area([4, 3, 2, 1, 4]))


if __name__ == "__main__":
    assert give_max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert give_max_area([1, 1]) == 1
    assert give_max_area([4, 3, 2, 1, 4]) == 16
    print("all tests passed")
