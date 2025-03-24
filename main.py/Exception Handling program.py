try:
    # Taking user input
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Performing division
    result = num1 / num2

    # Displaying the result
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

except ValueError:
    print("Error: Please enter valid numbers!")

except Exception as e:
    print("An unexpected error occurred:", e)

finally:
    print("Program execution completed.")
