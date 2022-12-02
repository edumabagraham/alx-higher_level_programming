#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        operator = sys.argv[2]

        if operator == '+':
            sum = add(a, b)
            print("{:d} + {:d} = {:d}".format(a, b, sum))
        elif operator == '-':
            difference = sub(a, b)
            print("{:d} - {:d} = {:d}".format(a, b, difference))
        elif operator == '*':
            product = mul(a, b)
            print("{:d} * {:d} = {:d}".format(a, b, product))
        elif operator == '/':
            quotient = div(a, b)
            print("{:d} / {:d} = {:d}".format(a, b, quotient))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
