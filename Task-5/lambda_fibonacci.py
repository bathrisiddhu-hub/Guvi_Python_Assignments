# Using lambda function to generate Fibonacci series up to n terms
n_terms = 10
fibonacci = lambda n: n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
print("Fibonacci series up to", n_terms, "terms:")
for i in range(n_terms):
    print(fibonacci(i), end=" ")