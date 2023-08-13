#列表使用

mags=["Zack","John","Alex"]

#for 的使用
for mag in mags:
   print(f'{mag.title()},you are marvelous')
   print(f"I can't wait to see you next show,{mag.title()}!\n")
print(list(mags))

#range的使用
numbers1=list(range(1,6))
numbers2=range(1,6)
#for number in numbers:
#print(range(1,6)[1])
print(numbers1)
print(numbers2)

squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square)
print(squares)

request_toppings=['mushrooms','green peppers','extra cheese']
for request_topping in request_toppings:
    if request_topping=='green peppers':
        print('Sorry!We are out of green peppers!')
    else:
        print(f'Adding {request_topping}')

request_toppings=[]
if request_toppings:
    for request_topping in request_toppings:
        if request_topping=='green peppers':
            print('Sorry!We are out of green peppers!')
        else:
            print(f'Adding {request_topping}')
else:
    print('Do you want a plain pizza?')

#if a < 1

