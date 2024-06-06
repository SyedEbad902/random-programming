def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    # Get the number from the user
    num = int(input("Enter a number to calculate its factorial: "))
    
    # Calculate the factorial
    result = factorial(num)
    
    # Print the result
    print(f"The factorial of {num} is {result}")

if __name__ == "__main__":
    main()
