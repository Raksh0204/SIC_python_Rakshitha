def sum_alternating_geometric_series(n, terms):

  if n == 1:
    return terms
  else:
    return (1 - (-n)**terms) / (1 + n)

# Example usage:
n = int(input("Enter the number: "))
terms = 10
result = sum_alternating_geometric_series(n, terms)
print(result)