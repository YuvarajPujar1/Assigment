n = int(input("Enter the number of integers: "))

# Initialize sum variable
total = 0

# Loop to get n numbers and add them
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    total += num

# Print the sum
print("The sum of the given numbers is:", total)