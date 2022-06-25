# Создайте класс и поля соответствующему вашему варианту (поля статические и динамические).
# Создайте три метода (класса, объекта и статический). Выберете поле или метод для реализации инкапсуляции.
# Пропишите запись и считывание (get, set) инкапсулированных полей.
#
# Kласс Airline: Пункт назначения, Номер рейса, Тип самолета, Время вылета, Дни недели.
# Функции- члены реализуют запись и считывание полей (проверка корректности).
# Создать список объектов. Вывести:
# список рейсов для заданного пункта назначения;
# б) список рейсов для заданного дня недели;

class Airline:
    __plainType = "Boeing"
    daysOfWeek = []

    def __init__(self, destination, flightNumber, plainType, departureTime, daysOfWeek):
        self.destination = destination
        self.flightNumber = flightNumber
        self.__plainType = plainType
        self.departureTime = departureTime
        self.daysOfWeek = daysOfWeek

    # методы класса
    def getPlainType(self):
        return self.__plainType

    def setplainType(self, plainType):
        self.__plainType = plainType

    def setDestination(self, destination):
        self.destination = destination

    def setFlightNumber(self, flightNumber):
        self.flightNumber = flightNumber

    def setPlainType(self, plainType):
        self.__plainType = plainType

    def setDepartureTime(self, departureTime):
        self.departureTime = departureTime

    def setDaysOfWeek(self, daysOfWeek):
        self.daysOfWeek = daysOfWeek

    # статический метод
    @staticmethod
    def getAirlineName():
        return "Etihad"

    # метод класса
    @classmethod
    def ibizaFlight(cls, flightNumber, departureTime, daysOfWeek):
        ibizaFlight = cls("Ibiza", flightNumber, "Airbus", departureTime, daysOfWeek)
        return ibizaFlight

madridFlight = Airline("Madrid", "B1423", "Bieing", "10:00", ["Monday", "Tuesday"])
londonFlight =  Airline("London", "A1234", "Airbus", "09:00", ["Saturday"])
amsterdamFlight1 = Airline("Amsterdam", "B4543", "Boeing", "11:00", ["Monday", "Friday", "Sunday"])
amsterdamFlight2 = Airline("Amsterdam", "B4500", "Airbus", "08:00", ["Monday"])
airlineList = list()
airlineList.append(madridFlight)
airlineList.append(londonFlight)
airlineList.append(amsterdamFlight1)
airlineList.append(amsterdamFlight2)

print("Введите пункт назначения")
destination = input()

for flight in airlineList:
    if flight.destination.lower() == destination.lower():
        print(f"Номер рейса: {flight.flightNumber}")
        print(f"Тип самолета: {flight.getPlainType()}")
        print(f"Время вылета: {flight.departureTime}")
        print(f"Дни недели: {flight.daysOfWeek}")
