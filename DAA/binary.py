import random

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    search_steps = 0

    while low <= high:
        mid = (low + high) // 2
        search_steps += 1

        if arr[mid] == target:
            return mid, search_steps
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, search_steps


arr = list(range(1, 10000))
targets = random.sample(range(1, 10000), 100)
total_search_time = 0
successful_searches = 0

for t in targets:
    result, search_steps = binary_search(arr, t)
    
    if result != -1:
        successful_searches += 1
        total_search_time += search_steps
        print(f"Element {t} found at index {result + 1}")
    else:
        print(f"Element {t} not found")

if successful_searches > 0:
    avg = total_search_time / successful_searches
    print(f"Average search time: {avg}")
else:
    print("No successful searches to calculate average search time")
