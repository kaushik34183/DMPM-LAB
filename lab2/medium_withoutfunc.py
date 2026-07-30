# Input number of data points
n = int(input("Enter the number of data points: "))
data = []
for i in range(n):
    num = int(input("Enter data point: "))
    data.append(num)
data.sort()
if n % 2 == 0:
    median = (data[n//2 - 1] + data[n//2]) / 2
else:
    median = data[n//2]
print("Median =", median)