
n = int(input("Enter the number of data points: "))
sum = 0
for i in range(n):
    num = float(input("Enter data point: "))
    sum = sum + num
mean = sum / n
print("Mean =", mean)