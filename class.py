class Dog:
    '''模拟小狗的尝试'''

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        '''模拟小狗坐下的指令'''
        print(f'{self.name} is now sitting')

    def roll_over(self):
        '''模拟小狗打滚的指令'''
        print(f"{self.name} rolled over")

my_dog = Dog('Willy',6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()