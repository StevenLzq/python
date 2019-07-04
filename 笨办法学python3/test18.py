def print_two(*args):
    arg1,arg2=args
    print('arg1:{},arg2:{}'.format(arg1,arg2))

def print_two_again(*args):
    arg1,arg2=args
    print('arg1:{},arg2:{}'.format(arg1,arg2))


def print_one(arg1):
    print('arg1:{}'.format(arg1))


def print_none():
    print('io got none')


print_two('li','huang')
print_two_again('li','huang')
print_one('li')
print_none()