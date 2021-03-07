testCase = int(input())
li = []
lis =[]
price = []
pricer = 0
lol = []
for a in range(testCase):
    lol.append(a+1)
    cards = int(input())
    for i in range(cards):
        i = str(input())
        li.append(i)
        lis = li
        li = sorted(li)
        if lis != li:
            pricer += 1
    price.append(pricer)
    lis = []
    li = []
    pricer = 0
for x in range(testCase):
    print("Case #" + str(lol[x]) + ": " + str(price[x]))