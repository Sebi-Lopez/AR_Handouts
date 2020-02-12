print("Hello darkness")

gerard = True
gerardNom = "Clotet"
gerardNumber = 100
gerardNomfromNumber = format(54)
print(gerard)
print(gerardNom)
print(gerardNumber)
print(gerardNomfromNumber)

numberINPT = input("Introduce number: ")
print(numberINPT)

number = 100

if number > 100:
    print("El gerard es grandote")
elif number < 100:
    print("El gerard no en te ni idea")
else: 
    print("100 es 100")


running = True

while running:
    number+=1
    print(number)

    if number >= 500:
        running = False
    
else: 
    print("Loop is over")

for i in range(5,20):
    print(i)

else: print("For loop is over")

def getSize():
    return (30,50)

width, height = getSize()
print(width, height)

def hello(a, b):
    return a + b

print(hello(2,5))