def is_prime(n):
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

def prime_digit_sum(n):
  total = 0
  while n:
    digit = n % 10
    if digit in [2, 3, 5, 7]:
      total += digit
    n //= 10
  return total

def is_prime_digit_sum_prime(n):
  return is_prime(prime_digit_sum(n))

num = int(input("Enter a number: "))
print(is_prime_digit_sum_prime(num))  