#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, div, mul, sub
    a = 10
    b = 5

    sum = add(a, b)
    difference = sub(a, b)
    product = mul(a, b)
    quotient = div(a, b)

    print("{:d} + {:d} = {:d}".format(a, b, sum))
    print("{:d} - {:d} = {:d}".format(a, b, difference))
    print("{:d} * {:d} = {:d}".format(a, b, product))
    print("{:d} / {:d} = {:d}".format(a, b, quotient))
