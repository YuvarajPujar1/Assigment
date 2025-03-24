# Creating an empty dictionary
employee = {}

# Adding values to the dictionary
employee["name"] = "Alice"
employee["age"] = 30
employee["department"] = "HR"

print("Initial Dictionary:", employee)

# Updating a value
employee["age"] = 31  # Changing age
print("\nAfter Updating Age:", employee)

# Adding a new key-value pair
employee["salary"] = 50000
print("\nAfter Adding Salary:", employee)

# Deleting a key-value pair using del
del employee["department"]
print("\nAfter Deleting Department:", employee)

# Removing a key-value pair using pop()
removed_value = employee.pop("age", "Key not found")
print("\nAfter Using pop() on Age:", employee)
print("Removed Value:", removed_value)

# Discard operation (Not available for dictionaries, but we can use pop() safely)
if "name" in employee:
    employee.pop("name")
print("\nAfter Discarding Name:", employee)

# Clearing the dictionary
employee.clear()
print("\nAfter Clearing Dictionary:", employee)
