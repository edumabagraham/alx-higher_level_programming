#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    
    a, operator, b = int(argv[1]), argv[2], int(argv[3])
    arithmetic = {'+': add, '-': sub, '*': mul, '/': div}

    if operator not in arithmetic:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{:d} {} {:d} = {:d}".format(a, operator, b, arithmetic[operator](a, b)))

    # day = {'m': "monday", 't': "tuesday"}
    # day_letter = argv[1]
    # if day_letter not in day:
    #     print("Not a day")
    #     exit(1)
    # print('{:s}'.format(day[day_letter]))