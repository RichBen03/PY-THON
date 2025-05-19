def find(target, numbers):
    for x in range(len(numbers)):
        if numbers[x]==target:
            return x
    return -1

print(find(39,[88,78,66,49,33,24,57,29,44,26]))
print(find(24,[88,78,66,49,33,24,57,29,44,26]))