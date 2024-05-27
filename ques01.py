number = 5
def factorial_iterative(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

result_iterative = factorial_iterative(number)
print(f"Factorial of {number} (iterative): {result_iterative}")
