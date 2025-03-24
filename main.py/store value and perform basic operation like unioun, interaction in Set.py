# Creating two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Display the sets
print("Set 1:", set1)
print("Set 2:", set2)

# Union of two sets
union_set = set1.union(set2)
print("\nUnion of Set1 and Set2:", union_set)

# Intersection of two sets
intersection_set = set1.intersection(set2)
print("Intersection of Set1 and Set2:", intersection_set)

# Difference (Elements in Set1 but not in Set2)
difference_set = set1.difference(set2)
print("Difference (Set1 - Set2):", difference_set)

# Symmetric Difference (Elements in either Set1 or Set2, but not both)
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric Difference:", symmetric_difference_set)
