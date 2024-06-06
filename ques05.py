import random
from statistics import mean, median, mode

# Generate a list of random numbers
random_numbers = [random.randint(1, 100) for _ in range(20)]

# Sort the list
sorted_numbers = sorted(random_numbers)

# Calculate mean, median, and mode
mean_value = mean(sorted_numbers)
median_value = median(sorted_numbers)
mode_value = mode(sorted_numbers)

# Print the results
print("Random Numbers: ", random_numbers)
print("Sorted Numbers: ", sorted_numbers)
print("Mean: ", mean_value)
print("Median: ", median_value)
print("Mode: ", mode_value)
