def square(number):

    if number <= 0 or number > 64: raise ValueError("square must be between 1 and 64")

    sum_total = 2**(number-1)
    return sum_total

def total():
    sum_total = 0
    
    for times in range(0,64):
        sum_total += 2**(times)
    return sum_total
    
