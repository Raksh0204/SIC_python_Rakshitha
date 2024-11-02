<<<<<<< HEAD
def nth_digit(num, n, left_to_right=True):

  if n <= 0:
    return -1

  if left_to_right:
    while n > 1:
      num //= 10
      n -= 1
  else:
    while n > 1 and num > 0:
      num %= 10 // n
      n -= 1

  return num % 10

num = int(input("Enter a number: "))
n = int(input("Enter the position: "))
direction = input("Enter 'left' or 'right': ")

if direction == 'left':
  digit = nth_digit(num, n)
else:
  digit = nth_digit(num, n, False)

if digit == -1:
  print("Invalid position.")
else:
=======
def nth_digit(num, n, left_to_right=True):

  if n <= 0:
    return -1

  if left_to_right:
    while n > 1:
      num //= 10
      n -= 1
  else:
    while n > 1 and num > 0:
      num %= 10 // n
      n -= 1

  return num % 10

num = int(input("Enter a number: "))
n = int(input("Enter the position: "))
direction = input("Enter 'left' or 'right': ")

if direction == 'left':
  digit = nth_digit(num, n)
else:
  digit = nth_digit(num, n, False)

if digit == -1:
  print("Invalid position.")
else:
>>>>>>> b362549bb6df76c52e026eea85baee30b981ede2
  print("The nth digit is:", digit)