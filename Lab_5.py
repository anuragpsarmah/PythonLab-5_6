# QUESTION 1

while True:
    try:
        num1 = int(input("Enter a numerator: "))
        num2 = int(input("Enter a denominator: "))
        result = num1 / num2
        print(f"The result is {result}")
        break 
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Please enter valid integer values for numerator and denominator.")
    finally:
        print("Program execution completed.")
print('\n')





#QUESTION 2

while True:
    try:
        my_list = [1, 2, 3]
        index = int(input("Enter an index: "))
        result = my_list[index]
        print(f"Element at index {index} is: {result}")
        break

    except IndexError:
        print("Index is out of bounds.")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")

    finally:
        print("Execution completed.")




