# return the nth value in the fibonacci series.
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))


# returns the nth value in the lucas numbers
def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return (lucas(n-1) + lucas(n-2))


# return series sum
def sum_series(n, x=0, y=1):
    if n == 0:
        return x
    elif n == 1:
        return y
    else:
        return (sum_series((n-1), x, y) + sum_series((n-2), x, y))
