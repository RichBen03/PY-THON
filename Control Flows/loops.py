numbers = [1, 5, 3, 9]

# total = 0
# for end in numbers:
#     total = end + total
# average = total / len(numbers)
# print(f"The total sum of the numbers in the list is {total}")
# print(f"The average of the numbers is {average}")
# largest=numbers[0] # Assume the largest number is the first position
# for num in numbers:
#     if num > largest:
#         largest = num
# print(f"The largest number is {largest}")

# even = 0
# for num in numbers:
#     if num % 2 == 0:
#         even = even + num

# print(f"The sum of even numbers is:{even} ")

def factorial(n):
    if n > 1:
        fact = n-1
        total = n * fact
        print(total)
factorial(4)


