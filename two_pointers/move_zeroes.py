"""Move Zeroes (LeetCode 283)

Given a list of integers nums, move all the 0s to the end, keeping the non-zero numbers in their original order. Do it in place: modify nums directly, with no copy of the list.

[0, 1, 0, 3, 12] → [1, 3, 12, 0, 0]
[0] → [0]
[1, 2, 3] → [1, 2, 3]

"""

# def push_zeroes_to_right(arr):
#     slow = 0
#     fast = 0
#     while fast < len(arr) and slow < len(arr):
#         # slow should seek 0 and fast should seek non zero and replace places
#         # range no -1 and with len -1 is needed
#         if arr[fast] == 0:
#             fast += 1
#             continue
#         if arr[slow] != 0 :
#             slow += 1
#             continue
#         if slow > fast:
#             fast = slow
#             continue

#         arr[slow], arr[fast] = arr[fast], arr[slow]
        
#     return arr

# slow = 0                          # where the next good item goes
# for fast in range(len(arr)):      # fast checks every item
#     if <arr[fast] is good>:       # keep it?
#         arr[slow] = arr[fast]     # or swap, if the bad ones must stay in the list
#         slow += 1                 # move slow only when you keep something
def push_zeroes_to_right(arr):
    slow = 0
    for fast in range(len(arr)):
        if arr[fast] != 0:
            if slow != fast:
                arr[slow], arr[fast] = arr[fast], arr[slow]
            slow+=1
        
    return arr

# print(push_zeroes_to_right([2,0,1]))


if __name__ == "__main__":
    assert push_zeroes_to_right([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
    assert push_zeroes_to_right([0]) == [0]
    assert push_zeroes_to_right([1, 2, 3]) == [1, 2, 3]
    assert push_zeroes_to_right([]) == []
    print("all tests passed")
