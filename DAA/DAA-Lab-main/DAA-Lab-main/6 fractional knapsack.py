class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight


def \
        knapsack(items, capacity):
    for item in items:
        item.ratio = item.value / item.weight

    items.sort(key=lambda item: item.ratio, reverse=True)

    total_value = 0
    total_weight = 0
    chosen_items = []

    for item in items:
        if total_weight + item.weight <= capacity:
            total_weight += item.weight
            total_value += item.value
            chosen_items.append((item, 1.0))
        else:
            chosen_part = capacity - total_weight
            chosen_fraction = chosen_part / item.weight
            chosen_value = chosen_fraction * item.value
            total_weight += chosen_part
            total_value += chosen_value
            chosen_items.append((item, chosen_fraction))

    return total_value, total_weight, chosen_items


items = [
    Item(60, 10),
    Item(100, 20),
    Item(120, 30)
]
capacity = 50
total_value, total_weight, chosen_items = knapsack(items, capacity)

print(f"Total value in knapsack = {total_value}")
print(f"Total weight in knapsack = {total_weight}")
print("Items chosen:")
print('value    weight   ratio   fraction')
for item, fraction in chosen_items:
    print(f"  {item.value}       {item.weight}     {item.ratio}        {fraction}")
