def steps(number):

    count = 0
    number = round(number)
    
    if number <= 0: raise ValueError("Only positive integers are allowed")
    
    while number != 1:
        if number % 2 == 0: 
            number //= 2
            count += 1
        else:
            number *= 3
            number += 1
            count += 1
        
    return count
