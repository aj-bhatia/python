# Ajay Bhatia
# FizzBuzz
# Script to perform the classic programming problem, FizzBuzz.

if __name__ == "__main__":
    # Loop from 1 to 100
    for i in range(1, 101):
        r3 = i % 3
        r5 = i % 5
        # check if divisible by 3
        if not r3:
            print("Fizz", end='')
        # check if divisible by 5
        if not r5:
            print("Buzz", end='')
        # if not divisible by both, print just the number
        if r3 and r5:
            print(i, end='')
        print()
