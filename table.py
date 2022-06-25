class Truck:
    tables = []
    totalMass = 0
    def __init__(self, tonnage):
        self.tonnage = tonnage
        self.isFull = False
    def addTable(self, table):
        self.totalMass += table.mass
        if (self.totalMass > self.tonnage):
            self.isFull = True
            print("Too many tables")
        else:
            self.tables.append(table)
            print("Added " + str(table.mass))


class Table:
    def __init__(self, mass):
        self.mass = mass

truck = Truck(100)

t1 = Table(20)
t2 = Table(30)
t3 = Table(40)
t4 = Table(50)
t5 = Table(60)
t6 = Table(70)

tableList = [t1, t2, t3, t4]

for table in tableList:
    if (not truck.isFull):
        truck.addTable(table)
    else:
        break;