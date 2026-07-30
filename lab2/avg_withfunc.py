# Function to calculate mean
def find_mean(data):
    total = 0

    for num in data:
        total = total + num

    mean = total / len(data)
    return mean

n = int(input("Enter the number of data points: "))

data = []

for i in range(n):
    num = float(input("Enter data point: "))
    data.append(num)

result = find_mean(data)

print("Mean =", result)