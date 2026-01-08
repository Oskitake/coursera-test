def equilateral(sides):

    a = sides[0]
    
    if a > 0 and sides.count(a) == 3 :
        return True
    return False

def isosceles(sides):
    
    a = sides[0]
    b = sides[1]
    c = sides[2]

    if a + b >= c and b + c >= a and a + c >= b and sides.count(0) == 0:
        if  (a > 0 and sides.count(a) >= 2) or (b > 0 and sides.count(b) == 2):
            return True
    return False

def scalene(sides):

    a = sides[0]
    b = sides[1]
    c = sides[2]

    if a + b >= c and b + c >= a and a + c >= b and sides.count(0) == 0 and a != b != c and a != c != b:
        return True
    return False
