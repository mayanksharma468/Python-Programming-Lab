d1={'a':100,'b':200,'c':400}
d2={'a':200,'b':100,'c':400}
for i in d2:
    d2[i]=d1[i]+d2[i]
counter=d2
print(counter)
