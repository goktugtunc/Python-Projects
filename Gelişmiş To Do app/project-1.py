def add():
    global liste
    y = input("\nWhat would you like me to add? : ")
    liste.append(y)

def show():
    global liste
    i = 1
    print("\n")
    for y in liste:
        print(str(i) + "-", y)
        i += 1

def delete():
    global liste
    print("\n")
    show()
    x = int(input("Which number do you want to delete?"))
    liste.pop(x - 1)

i = 1
liste = []
while(i != 0):
    x = int(input("What would you like to do? : 1-add 2-show 3-delete 4-exit program\n"))
    if(x == 1):
        add()
    elif(x == 2):
        show()
    elif(x == 3):
        delete()
    elif(x == 4):
        print("Okey, I am exit this program!")
        i = 0
    else:
        print("OUPS! You entered an invalid data!")
        print("Please try again!")