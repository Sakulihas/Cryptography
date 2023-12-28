# Erling Ringkjob
# MATH 4440
# The extended version of the Eucliden Algorithm


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


#function ext_euclid_algo, returns the tuple (y, x - q * y),
#upon calling the above function, the results get assign to separate variables (result_x and result_y).
#This should resolve the TypeError you were encountering.
def ext_euclid_algo(a, b, c):
    if b == 0:
        return 1, 0

    quote, remaind = division(a, b)

    x, y = ext_euclid_algo(b, remaind, c)

    return y, x - quote * y

a = 61
b = 35
c = 1
res_card_x, res_card_y = ext_euclid_algo(a, b, c)
print("Extended GCD Result: x =", res_card_x, ", y =", res_card_y)