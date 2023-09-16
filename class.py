class Dog:
    '''模拟小狗的尝试'''

    def __init__(self,name,age):
        '''初始化属性name和age'''
        self.name = name
        self.age = age

    def sit(self):
        '''模拟小狗坐下的指令'''
        print(f'{self.name} is now sitting')

    def roll_over(self):
        '''模拟小狗打滚的指令'''
        print(f"{self.name} rolled over")

# my_dog = Dog('Willy',6)

# print(f"My dog's name is {my_dog.name}.")
# print(f"My dog is {my_dog.age} years old.")
# my_dog.sit()
# my_dog.roll_over()


#使用类和实例的属性和方法
class Car:
    '''模拟汽车的尝试'''
    
    def __init__(self,make,model,year):
        '''初始化描述汽车的属性'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.long_name = ''
        
    def get_descriptive_name(self):
        '''返回规范的车辆属性信息'''
        self.long_name = f'{self.year} {self.make} {self.model}'
        
    def read_odometer(self):
        '''打印车辆的里程'''
        print(f'My {self.long_name} has {self.odometer_reading} miles on it.')

    def update_odometer(self,mileage):
        self.odometer_reading = mileage

my_new_car = Car('audi','a4',2024)
my_new_car.get_descriptive_name()
print(my_new_car.long_name)
my_new_car.update_odometer(23)
my_new_car.read_odometer()