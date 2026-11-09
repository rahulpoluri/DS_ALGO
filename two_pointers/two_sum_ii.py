"""Two Sum II, Sorted Input (LeetCode 167)

Given a list of integers numbers that is already sorted in ascending order, find two numbers that add up to target. Return their positions, 1-indexed, as [index1, index2]. There is exactly one solution, and you can’t use the same element twice.

numbers = [2, 7, 11, 15], target = 9 → [1, 2]
numbers = [2, 3, 4], target = 6 → [1, 3]
numbers = [-1, 0], target = -1 → [1, 2]

Constraint: use O(1) extra space."""

def find_two_sum(array, k):
    left, right = 0, len(array)-1
    while left<right:
        summ = array[left]+array[right] 
        if summ < k:
            left+=1
        elif summ > k:
            right-=1
        else:
            return [left+1, right+1]
        
    return -1

# print(find_two_sum([2, 3, 4], 6))


if __name__ == "__main__":
    assert find_two_sum([2, 7, 11, 15], 9) == [1, 2]
    assert find_two_sum([2, 3, 4], 6) == [1, 3]
    assert find_two_sum([-1, 0], -1) == [1, 2]
    print("all tests passed")
