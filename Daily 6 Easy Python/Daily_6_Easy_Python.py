from decimal import Decimal, getcontext

# credit for this algorithm goes to Chris Hills
# http://www.codeproject.com/Articles/11692/Calculate-pi-to-one-million-decimal-places

def calc_pi(precision = 30):

    pi = Decimal(4) * (Decimal(4) * inverse_tangent(Decimal(1)/Decimal(5), precision + 2) - inverse_tangent(Decimal(1)/Decimal(239), precision + 2))

    l = list(str(pi))
    l.pop()
    l.pop()
    new_pi = ''.join(l)

    return new_pi

def inverse_tangent(value, precision):
    i = 0
    getcontext().prec = precision
    result = Decimal(0)
    s = Decimal(1)

    while True:
        old_result = result
        x = Decimal(2*i + 1)
        result += Decimal(s*((value**x)/x))
        s *= Decimal(-1)
        i += 1
        if old_result == result:
            break

    return result

print(calc_pi())