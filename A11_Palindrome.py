<<<<<<< HEAD
num = int(input("Enter a number: "))

original_num = num
reversed_num = 0

while num > 0:
  digit = num % 10
  reversed_num = reversed_num * 10 + digit
  num //= 10

if original_num == reversed_num:
  print(original_num, "is a palindrome.")
else:
=======
num = int(input("Enter a number: "))

original_num = num
reversed_num = 0

while num > 0:
  digit = num % 10
  reversed_num = reversed_num * 10 + digit
  num //= 10

if original_num == reversed_num:
  print(original_num, "is a palindrome.")
else:
>>>>>>> b362549bb6df76c52e026eea85baee30b981ede2
  print(original_num, "is not a palindrome.")