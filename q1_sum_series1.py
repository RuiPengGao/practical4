#q1_sum_series1


i = int(input("Enter number here:"))

def sum_series(i):
    if i == 1:
        return 1
    else:
        return 1 / i + sum_series(i - 1)

print("{0:.3f}".format(sum_series(i)))
