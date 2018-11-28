

def generator(n):
    i = 0
    while i < 0:
        print("i ###")
        i += 1
        print('2 ###')

for x in generator(5):
    print("------", x)

print("**************************************************************")

def yieldGenerator(n):
    i = 0
    while i < n :
        print("1 ###")
        yield i 
        i += 1
        print("2 ###")
for x in yieldGenerator(5):
    print('------', x)