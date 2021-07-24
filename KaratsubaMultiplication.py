import time


def multiply(x, y):

    if x < 10 or y < 10:
        return (x * y)

    n = max(len(str(x)), len(str(y)))

    # temp = max(x, y)
    # n = 0
    # while temp > 0:
    #     temp = temp // 10
    #     n += 1
    # print(f'N : {n} , n/2 : {n/2}, round : {round(n/2)}, true/false : {round(n/2)*2 == n}')
    a = x // (10 ** round(n / 2))
    b = x % (10 ** round(n / 2))
    c = y // (10 ** round(n / 2))
    d = y % (10 ** round(n / 2))
    ac = multiply(a, c)
    bd = multiply(b, d)
    z = multiply((a + b), (c + d))
    diff = (z - ac - bd)

    return (10 ** (round(n / 2) * 2)) * ac + ((10**round(n / 2)) * diff) + bd


x = 3141592653589793238462643383279502884197169399375105820974944592

y = 2718281828459045235360287471352662497757247093699959574966967627


t = multiply(x, y)


# def Karatsuba(x, y):
