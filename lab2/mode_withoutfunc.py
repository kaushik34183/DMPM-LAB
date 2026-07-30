# Enter data points separated by space
data = list(map(int, input("Enter data points: ").split()))

mode = data[0]
max_count = 0

for i in data:
    count = 0
    for j in data:
        if i == j:
            count += 1
    if count > max_count:
        max_count = count
        mode = i

print("Mode =", mode)