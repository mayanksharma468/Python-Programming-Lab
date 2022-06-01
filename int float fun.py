def distance_from_zero(num):
    if num not in (('a'>=num and 'z'<=num)or ('A'>=num and 'Z'<=num)):
        return num
    else:
        return 'Nope'
print(distance_from_zero('what'))
