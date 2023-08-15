# prompt = 'If you share your name,we wil be pleased. '
# prompt += '\nWhat is your name:'
# name = input(prompt)
# print(f"Hello! {name}")

# age = input("How old are you?: ")
# print(age)
# if int(age) >= 18:
#     print("You die")

# current_number = 1
# while current_number != 5:
#     print(current_number)
#     current_number += 1

#多种while停止循环的方法
#(1)判断字符串是否为quit
# current_string = ""
# while current_string != "quit":
#     current_string=input("Enter 'quit' to stop the program: ")
#     if current_string != "quit":
#         print(f'The current string is {current_string}')

#(2)判断是否为True
# current_string = ""
# active = True
# while active:
#     current_string=input("Enter 'quit' to stop the program: ")
    
#     if current_string == "quit":
#         active = False
#     else:
#         print(f'The current string is {current_string}')

#(3)用Break停止循环
# current_string = ""
# active = True
# while active:
#     current_string=input("Enter 'quit' to stop the program: ")
    
#     if current_string == "quit":
#         break
#     else:
#         print(f'The current string is {current_string}')

#使用while调整列表中的值
# unconfirmed_users = ['alice','brian','candace']
# confirmed_users = []
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     print(f"Verifing user: {current_user.title()}")
#     confirmed_users.append(current_user)

# for confirmed_user in confirmed_users:
#     print(f"{confirmed_user.title()} has been confired")

#使用while操作字典
responses = {}
repeat = True

while repeat:
    name = input("What's your name? ")
    response = input("What mountain are you willing to climb?")
    responses[name] = response
    answer = input("Would you like to recommend another person to respond?(yes/no)")
    if answer != "yes":
        repeat = False

print("\n---Poll Results:---")
for name,response in responses.items():
    print(f"{name.title()} would like to go to {response}")




    
    