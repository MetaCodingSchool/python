
# primer
guests= ['Zharas','Sanzhar', 'Batman']  
objects = [8,12.6, "Hello", True]


print(guests)
print(objects)

guests=["Zharas", "Sanzhar","Nurlybek", "Almaz","Yerbol"]
print(guests[0]) #Zharas
print(guests[1]) #Sanzhar
print(guests[3]) #Almaz


guests[3]='Marlen'
print(guests[0]) #Zharas
print(guests[1]) #Sanzhar
print(guests[3]) #Marlen


guests=["Zharas", "Sanzhar","Nurlybek", "Almaz","Yerbol"]
for person in guests:
    print(person)


guests=["Zharas", "Sanzhar","Nurlybek", "Almaz","Yerbol"]

#Добавляем в конец списка
guests.append("Yerbol")  #["Zharas", "Sanzhar","Nurlybek", ,"Yerbol"]
#Добавляем на вторую позицию
guests.insert(1,"Marlen ")  #["Zharas","Marlen", "Sanzhar","Nurlybek", ,"Yerbol"]
#Получаем индукс элемента
index_of_sanzhar=guests.index("Sanzhar")
#удаляем по этому индексу
removed_item=guests.pop(index_of_sanzhar)   #["Zharas","Marlen","Nurlybek", ,"Yerbol"]
#удаляем последний элемент 
last_item=guests.pop() #["Zharas","Marlen","Nurlybek",]
print(guests) #["Zharas","Nurlybek",]
#удаляем все элементы
guests.clear()


guests=["Zharas", "Nartay","Marlen", "Nurlybek","Yerbol"]
guests.sort()
print(guests)

numbers = [4,1, 35,12,101,9,56]
numbers.sort()
print(numbers)





guests=[
    ["Zaras",1],
    ["Marlen",9],
    ["Nurlybek",15],
    ["Yerbol",3],
]



print(guests[0])             #["Zharas",1]
print(guests[0] [0])         #Zharas
print(guests[0] [1])         #1
print(guests[2] [0])         # Nurlybek
print(guests[3] [1])         #3
# #

my_car=('Toyota', 'Camry', 2.5 , 2014)
print(my_car)

quests = ["Zaras", "Marlen" , "Nurlybek", "Yerbol"]
print(quests)    # ["Zaras", "Marlen" , "Nurlybek", "Yerbol"]

my_guests =  tuple(quests)
print(my_guests)      # ["Zaras", "Marlen" , "Nurlybek", "Yerbol"]

# #
my_car = ("Toyota", "Camry", 2.5 , 2014 )
print(my_car[0])  #Toyota
print(my_car[1])  #Camry
print(my_car[3])  #2014

brand, model, engine, year = ('Toyota', "Camry", 2.5 , 2014 )
print(brand)    #Toyota
print(model)    #Camry
print(year)    #2014


my_car = ("Toyota", "Camry", 2.5 , 2014 )
i = 0
while i < len(my_car):
    print(my_car[i])
    i+=1


presidents= {'Kazakhstan': "Tokaev", 'Russia': "Putin", 'USA': "Boden"}

kasha = {1: "Zharas", "2": True,9:13.6}

presidents={'Kazakhstan': "Tokaev", 'Russia': "Putin", 'USA': "Boden"}
print(presidents['Kazakhstan'])   #Tokaev















