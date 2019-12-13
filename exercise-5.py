# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.


# Hint: The next number is found by adding the two numbers before it

# 0,1,1,2,3,5,8,13,21,34...
# -2,-1,^
# f(n): f(n-1) + f(n-2)
# 5 = 3 + 2
# c = a + b

term = 0 
a = 0 
b = 1
c = a + b

while term <= 50:
    # term: 0 / number: 0 
    print(f'term: {term} / number: {a}')
    a = b
    b = c
    c = a + b
    term += 1
