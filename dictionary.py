alien_0={}
alien_0['color']='green'
alien_0['points']=5
alien_1=['green','5']

#print(alien_0)
#print(alien_0["color"])
#print(alien_0['color'])

#print(alien_1[1])

alien_0["x_position"]=0#添加键值对
#print(alien_0)

alien_0["x_position"]=2#修改键值对
#print(alien_0)

del alien_0['x_position']#删除键值对
#print(alien_0)

fav_lan={
    'Jen':'c',
    'Ken':'python',
    'Mary':'c++',
    }

# alien_1={'color': 'blue', 'points': 4}
# alien_2={'color': 'yelloe', 'points': 2}
# aliens=[alien_0,alien_1,alien_2]
# for alien in aliens:
#     print(alien)

#在列表中存储字典
aliens=[]
for alien_number in range(10):
    new_alien={'color': 'blue', 'points': 4}
    aliens.append(new_alien)

for alien in aliens[:3]:
    alien["color"]='yellow'

for alien in aliens[:5]:
    print(alien)

#在字典中存储列表
pizza={
    'crust':'thick',
    'toppings':['mushrooms','cheese'],
    }
print(f"You've ordered a {pizza['crust']}-crust pizza with toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")

fav_lan={
    'Jen':['c'],
    'Ken':['rust','python'],
    'Mary':['rust','c++'],
    }
for name,languages in fav_lan.items():
    if len(languages)==1:
        for language in languages:
            print(f"{name}'s favorite language is:")
            print(f"\t{language.title()}")
    else:
        print(f"{name}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")
    
    


