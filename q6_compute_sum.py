#compute sum
n = int(input("enter a number:"))

def sum_digits(n):
    s = str(n)
    if len(s) == 1:
        return n
    else:
        return int(s[0]) + sum_digits(int(s[1:]))

print("The sum is:", sum_digits(n))
