# def greeting_function(name):
#     """显示问候语"""
#     print(f"Hello {name.title()}")

# user_name = input("Please enter youe name: ")
# greeting_function(user_name)

#传递实参的多种方法
#位置实参
# def describe_animal(animal_type,animal_name):
#     '''显示宠物信息'''
#     print(f"\nI have a {animal_type}")
#     print(f"My {animal_type}'s name is {animal_name}")

# describe_animal('dog','Lucy')

#关键字实参
# describe_animal(animal_type = 'dog',animal_name = 'Lucy')


#返回值
# def get_formatted_name(first_name,last_name,middle_name=''):
#     '''返回标准形式的名字'''
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     return full_name.title()

# muscian = get_formatted_name('lance','stroll')
# print(muscian)

#返回字典
# def get_formatted_name(first_name,last_name,age=None):
#     '''返回个人信息字典'''
#     person = {
#         'first_name':first_name.title(),
#         'last_name':last_name.title(),
#     }
#     if age:
#         person['age'] = age
#     return person

# muscian = get_formatted_name('lance','stroll',age=17)
# print(muscian)

#包含循环
def get_formatted_name(first_name,last_name):
    '''返回标准个人姓名'''
    full_name = f"{first_name} {last_name}"
    return full_name.title()

print("Please tell us your name")
print("Please enter 'q' any time you want to quit ")

while True:
    first_name = input('First name: ')
    if first_name == "q":
        print('Thank you for playing this')
        break
    
    last_name = input('Last_name: ')
    if last_name == "q":
        print('Thank you for playing this')
        break
    
    person = get_formatted_name(first_name,last_name)
    print(f"Hello {person}!")