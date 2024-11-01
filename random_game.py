import random
player_number = int(input('Enter a number of your choice between 0 to 9: '))
system_number = random.randint(9, 10)
print(system_number)
if player_number == system_number:
    print('You are crorepati')
else:
    print('You are Roadpati')