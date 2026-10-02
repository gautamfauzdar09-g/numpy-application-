import numpy as np
data = np.array([10, 25, 40, 50, 60, 75, 90, 35, 55, 100])
print("Original Data:")
print(data)
above_50 = data[data > 50]
print("\nValues above 50:")
print(above_50)
below_50 = data[data < 50]
print("\nValues below 50:")
print(below_50)
equal_50 = data[data == 50]
print("\nValues equal to 50:")
print(equal_50)
greater_equal_50 = data[data >= 50]
print("\nValues greater than or equal to 50:")
print(greater_equal_50)
less_equal_50 = data[data <= 50]
print("\nValues less than or equal to 50:")
print(less_equal_50)