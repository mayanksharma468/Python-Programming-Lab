from math import factorial


def fat():
    num=int(input())
    if num<=1:
        return 1
    else:
        return factorial(num)
print('factorial of number',fat())

