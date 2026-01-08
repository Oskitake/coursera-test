def is_armstrong_number(number):
    n = number
    result = []
    sum_total = 0
    
    while n > 0:
        result.append(n % 10)
        n //= 10
    
    for digit in result:
        sum_total += digit**len(result)
    
    if number == sum_total: 
        return True
    return False