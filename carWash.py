def isFull():
    if len(car) == cap:
        return True
    else:
        return False


def menu():
    print("[1] to Enter Car\n")
    print("[2] to Remove Car\n")
    print("[3] to Know How many Cars in the Car Wash Machine\n")
    print("[4] to Know The Car In The Front\n")
    print("[0] to ShutDown\n")


def addCar():
    if (isFull() == False):
        customerName = input("Enter Customer Name\n")
        carNumber = input("Enter Car Number\n")
        if len(carNumber) == 10:
            if carNumber[0:2].isalpha() and carNumber[2:4].isnumeric() and carNumber[4:6].isalpha() and carNumber[6:10].isnumeric():
                service()
                washType = int(input("What Kind Of Wash?\n"))
                if washType == 1:
                    car.append([carNumber, customerName, "Normal Wash", 100])
                    print("Car Added\n")
                elif washType == 2:
                    car.append([carNumber, customerName, "Dry Wash", 200])
                    print("Car Added\n")
                elif washType == 3:
                    car.append([carNumber, customerName, "Wax Wash", 300])
                    print("Car Added\n")
                elif washType == 4:
                    car.append([carNumber, customerName, "Shiny Wash", 400])
                    print("Car Added\n")
                else:
                    print("Invalid Wash Type\n")
                    menu()
            else:
                print("Invalid Car Number\n")
        else:
            print("Invalid Car Number\n")
    else:
        print("Car Wash Is Full\n")


def removeCar():
    if len(car) != 0:
        print("Collect Rs."+str(car[0][3])+" From "+car[0][1]+"\n")
        car.pop(0)
        print("Now there are "+str(len(car))+" cars in the car wash machine\n")
    else:
        print("No Car In The Car Wash Machine\n")


def getDetail():
    if len(car) == 0:
        print("No Car In The Car Wash Machine\n")
    else:
        print(car[0][1], "'s Car is in Wash Machine\n")
        print("Car Number "+car[0][0]+" is inside machine\n")


def service():
    print("[1] to Normal Wash - Rs.100\n")
    print("[2] to Dry Wash -Rs.200\n")
    print("[3] to Wax Wash -Rs.300\n")
    print("[4] to Shiny Wash -Rs.400\n")


def getCount():
    print("There are", len(car), "cars in the car wash machine\n")




if __name__ == "__main__":
    print("Welcome To Chaitanya's Car Wash\n")
    cap = int(input("How Many Cars The Car Wash Can Contains\n"))
    car = []
    menu()
    sd=True
    option = input("Enter Your Option: \n")
    while (sd != False):
        if option == "1":
            addCar()
        elif option == "2":
            removeCar()
        elif option == "3":
            getCount()
        elif option == "4":
            getDetail()
        elif option =="0":
            if len(car) != 0:
                print("Wash All The Cars Before Shutting Down\n")
            else:
                break
        else:
            print("Invalid Option")
        menu()
        option = input("Enter Your Option: \n")
    print("Thank You For Visiting Chaitanya's Car Wash\n")
