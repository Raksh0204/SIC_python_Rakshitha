numbers1 = []
numbers2 = list()
numbers3 = [1, 2, 3, 4, 5]
numbers4 = list(numbers3)
numbers5 = list(numbers3[1:4])

print(numbers1)
print(numbers2)
print(numbers3)
print(numbers4)
print(numbers5)

input_size = int(input('Enter size of the Array: '))
numbers = []
for i in range(input_size):
    number = int(input())
    numbers.append(number)
    # numbers.append(int(input()))

print('The array is: ', numbers)

print(f'The array of size {input_size} is:')
for number in numbers:
    print(number, end='  ')

print()

print('Enter space seperated numbers in a line')
user_input = input()
print(type(user_input))

print()

numbers = [int(number) for number in user_input.split()]
print('The array is: ', numbers)

import sys
# Command line Args
# Find biggest and smallest numbers among the numbers given by user

print('User given numbers are: ', sys.argv)

print('Enter space seperated numbers in a line')

numbers = [int(number) for number in input().split()]
print('The array is: ', numbers)