a = ['hello' , 'to', 'java']
b = []
while len(a) != 0:
    b.append(min(a))
    a.remove(min(a))
print(b)