# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def sum_multiples(n):
    multiples = []
    for i in range(1, n):
        # print(input)
        if (i % 3 == 0 or i % 5 == 0):
            multiples.append(i)
        else: 
            continue

    # print(f"Multiples of 3 or 5 below {n}: {multiples}")

    sum_of_multiples = 0

    for multiple in multiples:
        sum_of_multiples = sum_of_multiples + multiple
    print(sum_of_multiples)



sum_multiples(1000)