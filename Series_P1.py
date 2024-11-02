def series(n, terms):

  if n == 1:
    return terms * n
  else:
    return n * (1 - n**terms) / (1 - n)

n = int(input("Enter the number : "))
terms = 10
result = series(n, terms)
print(result)