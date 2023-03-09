
# primer
a = int(input())
def square(a ):
    return a * a
b=square(a)
print(b)



# # primer 
def greeting():
    def hellow():print("helloe")
    def goodbye():print("Goodbye")

    hellow()
    goodbye()
greeting()


# primer
def city(name):
    print('name')

city("Almaty")

# primer
def city(name):
    print('City is: ', name)
def city(name,population):
    print(name, 'has population of', population)

print(city("Almaty", 300))

# primer
def sum (a,b):
    print(a+b)

def sum2(a,b):
    return a+b

sum(1,2)
sum2(1,2)



