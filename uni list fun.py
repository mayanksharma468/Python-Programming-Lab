def unilist():
    l=eval(input('enter list of number'))
    unil=[]
    for i in l:
        if i not in unil:
            unil.append(i)
    return unil
print(unilist())
