
i=0
num=[]

while i<6:
    print("at the top i is {}".format(i))
    num.append(i)
    i+=1
    print('number now',num)
    print("at the bottom i is {}".format(i))

print('the numbers:')
for i in num:
     print(i)

