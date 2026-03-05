# Project 3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?




prime_factors = []

def get_largest_prime_factor(n):

    
    q = 2
    x = n

    while q < 100:
        if float(x/2) % 2 == 0:
            # number is not a factor, does not divide evenly
            print(f"{n} divides evenly with {q}, it is a factor.")
            q = q + 1
        else:
            q = q + 1







get_largest_prime_factor(13195)


# 13195
# 600851475143