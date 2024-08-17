def knapsack_backtracking(weights, values, capacity):
    n = len(weights)
    max_value = [0]  # Use a list to allow updates within the nested function
    best_items = [0] * n
    
    def backtrack(i, current_weight, current_value, current_items):
        if i == n:
            if current_value > max_value[0]:
                max_value[0] = current_value
                best_items[:] = current_items[:]
            return
        current_items[i] = 0
        backtrack(i + 1, current_weight, current_value, current_items)
        if current_weight + weights[i] <= capacity:
            current_items[i] = 1
            backtrack(i + 1, current_weight + weights[i], current_value + values[i], current_items)
    
    backtrack(0, 0, 0, [0] * n)
    return max_value[0], best_items


weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5
max_val, items = knapsack_backtracking(weights, values, capacity)
print("Maximum value:", max_val)
print("Items included:", items)
