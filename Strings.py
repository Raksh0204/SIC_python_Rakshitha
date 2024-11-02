my_string = input('Enter a place name: ')

print(f'String in Upper case = {my_string.upper()}')
print(f'Type of {my_string} is {type(my_string)}')

for character in my_string: # for each loop
    print(f'{character}, Type={type(character)}')

print()

my_str = 'bengaluru'
print(my_str)
print(my_str[0])     # b
print(my_str[1])     # e
print(my_str[-1])    # u
print(my_str[-2])    # r

#print(my_str[-12])   IndexError
#print(my_str[100])   IndexError
print()
print(my_str[:])
print(my_str[::])

print(my_str[1:8])      # engalur
print(my_str[2:6:2])    # na
print(my_str[::2])      # bnauu
print(my_str[::-2])     # uuanb
print(my_str[::-1])     # urulagneb

print()

stri = 'banashankari'

print(stri.find('s'))           # 4
print(stri.find('m'))           # -1
print(stri.find('shankari'))    # 4
print(stri.find('a', 3))        # 3
print(stri.find('na', 1, 4))    # 2
print(stri.find('na', 1, 3))    # -1

print()

print(stri.index('s'))          # 4
print(stri.index('shankari'))   # 4
print(stri.index('a', 3))       # 3
print(stri.index('na', 1, 4))   # 2
#print(stri.index('na', 1, 3))  error
#print(stri.index('m'))         error

