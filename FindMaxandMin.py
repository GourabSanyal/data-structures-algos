arr = [32, 43, 76, 98, 132]
max = arr[0]
n = len(arr)

# Finding maximum

for i in range(0, n):
    if arr[i] > max:
        max = arr[i]

print(max)

# Finding min

min = arr[0]
n = len(arr)

for i in range(0, n):
    if arr[i] < min:
        min = arr[i]

print(min)
