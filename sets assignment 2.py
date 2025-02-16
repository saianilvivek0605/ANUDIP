set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
try_items = set1.symmetric_difference(set2)
desired_order = [20, 70, 10, 60]
try_items_sorted = sorted(try_items, key=lambda x: desired_order.index(x))
try_items_sorted_set = set(try_items_sorted)
print(try_items_sorted_set)
