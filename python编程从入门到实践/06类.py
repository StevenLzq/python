'''
class Dog():
#####################################模拟小狗###########################
    def __init__(self,name,age):
        self.name=name
        self.age=age


    def sit(self):
        print(self.name.title()+' is sitting .')

    def roll_over(self):
        print(self.name.title()+' is rolling over')


my_dog = Dog('willie',6)
print("my dog's name is "+my_dog.name.title())
print("my dog is "+str(my_dog.age)+' years old')
my_dog.sit()
my_dog.roll_over()


##################################9-1######################################

class Restaurant():
    def __init__(self,name,cuisine_type):
        self.name=name
        self.cuisine_type=cuisine_type

    def describe_restaurant(self):
        print('\nour hotel provide free_wifi')
        print('\n24_hour shower')

    def open_restaurant(self):
        print('\nout hotel is openning')

my_restaurant=Restaurant('rujia','sichuancai')
print("our hotel's name is "+my_restaurant.name.title())
print('our special cuisina is '+my_restaurant.cuisine_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()


'''
########################################################################
class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()

    def read_odometer(self):
        print('this car has '+str(self.odometer_reading)+' miles on it')
    def update_odometer(self,mileage):
        self.odometer_reading=mileage
        #将里程数设为定值 禁止回调
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print('you can not roll back odometer')
    def increment_odometer(self,miles):
        if miles>=0:

            self.odometer_reading+=miles
        else:
            print('the increment of miles must be wrong !')
my_car=Car('audi','a4',2006)
print(my_car.get_descriptive_name())


my_car.update_odometer(2350)
print(my_car.read_odometer())


my_car.increment_odometer(100)
print(my_car.read_odometer())

