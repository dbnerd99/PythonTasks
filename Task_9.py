"""
Calculate mean, median, and mode of a dataset.
Input: [1, 2, 2, 3, 4]
"""

from statistics import mean, median, mode

def calculations(value):
    value_mean = mean(value)
    value_median = median(value)
    value_mode = mode(value)

    return value_mean, value_median, value_mode

data = [1, 2, 2, 3, 4]
value_mean, value_median, value_mode = calculations(data)

print(f"Mean: {value_mean}")
print(f"Median: {value_median}")
print(f"Mode: {value_mode}")

"""
Output : 
Mean: 2.4
Median: 2
Mode: 2

Process finished with exit code 0
"""

