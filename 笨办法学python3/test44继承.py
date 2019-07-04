class Parent(object):
    def implicit(self):
        print("parent implicit()")

    def override(self):
        print("parent override()")

    def altered(self):
        print('patrent altered()')



class Child(Parent):
    def override(self):
        print('child override()')

    def altered(self):
        print('child before parent altered()')
        super(Child,self).altered()#在这里是用super调用了parent类的altered
        print('child after parent altered()')


dad=Parent()
son=Child()

dad.altered()
son.altered()

"""多重继承，是指继承了一个或多个类k"""