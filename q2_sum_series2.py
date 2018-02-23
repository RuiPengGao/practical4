#q2_sum_series2

i = int(input("Enter number here:"))

def sum_series(i):
    if i == 1:
        return 1/3
    else:
        return i/(2*i + 1) + sum_series(i - 1)

print("{0:.5f}".format(sum_series(i)))
