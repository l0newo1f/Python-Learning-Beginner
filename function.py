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


#使用循环的函数
# def get_formatted_name(first_name,last_name):
#     '''返回标准个人姓名'''
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# print("Please tell us your name")
# print("Please enter 'q' any time you want to quit ")

# while True:
#     first_name = input('First name: ')
#     if first_name == "q":
#         print('Thank you for playing this')
#         break
    
#     last_name = input('Last_name: ')
#     if last_name == "q":
#         print('Thank you for playing this')
#         break
    
#     person = get_formatted_name(first_name,last_name)
#     print(f"Hello {person}!")


#传递列表的函数
def print_name(user_names):
    for user_name in user_names:
        print(f'Hello {user_name.title()} !')

# names = ['eric','john','hame']
# print_name(names)


#在函数中修改列表


#在修改后函数不改变原列表值
#函数的实参使用list[:]即列表的副本，而不影响原列表


#传递任意数量(元组)的实参
def make_pizza(*toppings):
    '''打印披萨所有配料'''
    print("Making pizza with following toppings:")
    for topping in toppings:
        print(f"- {topping}")

# make_pizza('mushrooms','green peppers','cheese')
# make_pizza('mushrooms')

#传递任意数量(字典)的实参
def build_profile(first,last,**user_info):
    '''创建用户的字典信息'''
    user_info['first'] = first
    user_info['last'] = last
    return user_info

# user_profile = build_profile('albert','einstein',location = 'princeton',field = 'physics')
# print(user_profile)