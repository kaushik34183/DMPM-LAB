# Function to find median
def find_median(data):
    data.sort()
    n = len(data)

    if n % 2 == 0:
        median = (data[n//2 - 1] + data[n//2]) / 2
    else:
        median = data[n//2]

    return median



n = int(input("Enter the number of data points: "))

data = []

for i in range(n):
    num = int(input("Enter data point: "))
    data.append(num)

result = find_median(data)

print("Median =", result)