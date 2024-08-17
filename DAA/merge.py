count = 0
count2 = 0
dividing_steps = []
merging_steps = []

def merge_sort(arr):
    global count
    count += 1
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Append the dividing step to the global list
    dividing_steps.append(f"Dividing: {arr} into {left_half} and {right_half}")

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    merged_result = merge(left_half, right_half)

    # Append the merging step to the global list
    merging_steps.append(f"Merging: {left_half} and {right_half} -> {merged_result}")

    return merged_result

def merge(left, right):
    global count2
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        count2 += 1
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

# Example usage
arr = [30, 27, 43, 3, 9, 82, 10, 25, 17, 30,2,4,7,56,67,34]
# print(len(arr))
sorted_arr = merge_sort(arr)
print("Sorted Array: ", sorted_arr)
print("Count: ", count)
print("Count2: ", count2)

# Print dividing and merging steps at the end
print("\nDividing Steps:")
for step in dividing_steps:
    print(step)

print("\nMerging Steps:")
for step in merging_steps:
    print(step)
