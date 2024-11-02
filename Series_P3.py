def is_prime(num):

  if num <= 1:
    return False
  if num <= 3:
    return True
  if num % 2 == 0 or num % 3 == 0:
    return False

  i = 5
  while i * i <= num:
    if num % i == 0 or num % (i + 2) == 0:
      return False
    i += 6

  return True

def nth_prime(n):

  count = 0
  num = 2

  while count < n:
    if is_prime(num):
      count += 1
    num += 1

  return num - 1

n = int(input("Enter the number: "))
result = nth_prime(n)
print(result)