def is_prime(n):
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

def nth_term(n):
  if n % 2 == 1:
    count = 0
    num = 2
    while count < (n + 1) // 2:
      if is_prime(num):
        count += 1
      num += 1
    return num - 1
  else:
    return nth_term(n - 1) - nth_term(n - 3)

n = int(input("Enter a number: "))
print(nth_term(n)) 