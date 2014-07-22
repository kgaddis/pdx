# Kainoa Gaddis (c) 2014
# This program sums numbers from 1 to n

number = int(input("Type any number for n: "))
numbers = list(range(number + 1))
print(numbers)

i = 0
add = 0
while i <= number:
    print(numbers[i])
    add += i
    i += 1

print(add)
