#match case statement
x=int(input("enter number to select days of week"))

match x:
    case 1:
        print("The day is sunday")
    case 2:
        print("The day is monday")
    case 3:
        print("The day is tuesday")
    case 4:
        print("The day is wednesday")
    case 5:
        print("The day is thurday")
    case 6:
        print("The day is friday")
    case 7:
        print("The day is saturday")
    case _:
        print("Invalid Option")