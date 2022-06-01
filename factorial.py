def factorial_fun(n):
    sum=1
    if n<=0:
        return sum
    else:
        sum=1
        for i in range(1,n+1):
            sum=sum*i
        return sum
n=int(input())
result=factorial_fun(n)
print(result)
