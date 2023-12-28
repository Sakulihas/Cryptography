# Erling Ringkjob
# MATH 4440
# The general version of the Eucliden Algorithm



def division(a, b):
    assert a >= 0 and b > 0

    q = 0
    r = a 
    while r >= b:
        r -= b
        q += 1 
        assert r == a - q*b 
    return q,r 

def euclid_algo(a, b):
    assert a > b
    if b == 0:
        return a

    q, r = division(a, b)
    # The GCD
    common_val = euclid_algo(b, r)
    return common_val


#TODO:Come up with own test case

def euclid_test(res, x, y):
    gcd = euclid_algo(x,y)
    if (gcd == res):
        print(f"GCD OF x={x} and y={y} is {res}")
    else:
        print(f"GCD FAILED WITH x={x} and y={y}")

euclid_test(3, 183,105)