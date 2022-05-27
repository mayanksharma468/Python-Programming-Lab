z = open('info.txt')
data = z.readlines()
c =len(max(data,key=len))
for word in data:
    if len(word)== c:
        longest_word = word
print(longest_word)
z.close()
