import math

# Input data points
data = list(map(float, input("Enter data points: ").split()))
n = len(data)
total = 0
for i in data:
    total += i
mean = total / n
sum_sq = 0
for i in data:
    sum_sq += (i - mean) ** 2

variance = sum_sq / n
std = math.sqrt(variance)

print("Variance =", variance)
print("Standard Deviation =", std)