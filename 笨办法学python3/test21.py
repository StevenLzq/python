def add(a,b):
    print('adding {}+{}'.format(a,b))
    return a+b;

def subtract(a,b):
    print('subtracting {}-{}'.format(a,b))
    return a-b;
def multiply(a,b):
    print('multiplting {}*{}'.format(a,b))
    return a*b;
def divide(a,b):
    print('dividing {}/{}'.format(a,b) )
    return a/b;


print(' let us do some math with these functionj ')

age=add(3,5)

height=subtract(78,3)

weight=multiply(30,6)

iq=divide(100,2)

print('Age: {},Height:{},Weight:{},Iq:{}'.format(age,height,weight,iq))

f=subtract(add(24,divide(34,100)),1023)
print(f)