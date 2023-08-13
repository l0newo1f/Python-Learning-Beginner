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

current_string = ""
while current_string != "quit":
    current_string=input("Enter 'quit' to stop the program: ")
    if current_string != "quit":
        print(f'The current string is {current_string}')
    