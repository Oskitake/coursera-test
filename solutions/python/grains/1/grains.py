def square(number):

    if number <= 0 or number > 64: raise ValueError("square must be between 1 and 64")

    sum_total = 1
    if number > 1:
        for times in range(number-1):
            sum_total *= 2

    return sum_total

def total():
    sum_total = 18446744073709551615


    return sum_total
    
