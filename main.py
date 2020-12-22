from CassandraConnect import CassandraConnect

cassandra = CassandraConnect("tutorialspoint")


def show():
    data = cassandra.allCities()
    for i in range(len(data)):
        print(i, data[i].name, data[i].country)
    menu()


def create():
    name = input("write the name:")
    country = input("write the country:")
    data = cassandra.createCity(name, country)
    print(data)
    menu()


def update():
    data = cassandra.allCities()
    for i in range(len(data)):
        print(i, data[i].name, data[i].country)
    num = int(input("choice:"))
    choicedData = data[num]
    print("you choiced", choicedData.name)
    columns = ["name", "country"]
    for i in range(len(columns)):
        print(i, columns[i])
    k = int(input())
    column = columns[k]
    value = input("write the value:")
    updated = None
    if column == "name":
        updated = cassandra.update(id=choicedData.id, name=value)
    elif column == "country":
        updated = cassandra.update(id=choicedData.id, country=value)
    print(updated)
    menu()


def delete():
    data = cassandra.allCities()
    for i in range(len(data)):
        print(i, data[i].name, data[i].country)
    num = int(input())
    choicedData = data[num]
    print("you choiced", choicedData.name)
    deletedData = cassandra.delete(choicedData.id)
    print(deletedData)
    menu()


def menu():
    print("---Main Menu---")
    print("[1]Show Cities")
    print("[2]Create City")
    print("[3]Update City")
    print("[4]Delete City")
    print("[5]Exit")
    num = int(input("Choice:"))
    if num == 1:
        show()
    elif num == 2:
        create()
    elif num == 3:
        update()
    elif num == 4:
        delete()
    else:
        exit()


menu()
