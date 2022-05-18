def find_max_min(list_of_numbers):  # With divide and conquer

    if len(list_of_numbers) == 1:
        return list_of_numbers
    else:
        mid = len(list_of_numbers) // 2
        left = find_max_min(list_of_numbers[:mid])
        right = find_max_min(list_of_numbers[mid:])
        if left[-1] > right[0]:
            return left + right
        else:
            return right + left

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
B = find_max_min(A)
print(B)