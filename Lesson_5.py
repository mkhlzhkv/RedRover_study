class Car:

    adres = "город Москва, Красная площадь" #Адрес магазина

    def __init__(self, car_make, year, color, price, for_sale=False):
        self.car_make = car_make    #Марка автомобиля
        self.year = year    #Год выпуска
        self.color = color  #Цвет
        self.__price = price    #Цена
        self.__for_sale = for_sale  #Продается

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        print(f"Изменена стоимость автомобиля {self.car_make} с {self.__price} р. на {new_price} р.")
        self.__price = new_price
        print()

    def get_for_sale(self):
        return self.__for_sale

    def set_for_sale(self, new):
        self.__for_sale = bool(new)
        if new:
            print(f"Автомобиль {self.car_make} выставлен на продажу")
        else:
            print(f"Автомобиль {self.car_make} снят с продажи")
        print()

    def car_info(self):
        if self.__for_sale:
            print(f"В настоящее время продается автомобиль за {self.__price} р., который находится по адресу: {self.adres}:")
            print(f"{self.color} {self.car_make} {self.year} года выпуска")
        else:
            print(f"В настоящее время автомобиль {self.color} {self.car_make} {self.year} года выпуска не продается")
        print()

    @classmethod
    def change_adres(cls, new_adres):
        print(f"Изменен адрес магазина с {cls.adres} на {new_adres}")
        cls.adres = new_adres

    @staticmethod
    def add_car():
        print("Введите параметры автомобиля: Марка, Год выпуска, Цвет, Цена")
        car_make, year, color, price = input(), input(), input(), input()
        new_car = Car(car_make, year, color, price, True)
        return new_car

class FreightCar(Car):
    def __init__(self, car_make, year, color, price, for_sale, lifting_capacity=None):
        super().__init__(car_make, year, color, price, for_sale)
        self.lifting_capacity = lifting_capacity    #Грузоподъемность

    def car_info(self):
        if self.get_for_sale():
            print(f"В настоящее время продается автомобиль за {self.get_price()} р., который находится по адресу: {self.adres}:")
            print(f"{self.color} {self.car_make} {self.year} года выпуска с грузоподъемностью {self.lifting_capacity} тонн")
        else:
            print(f"В настоящее время автомобиль {self.color} {self.car_make} {self.year} года выпуска не продается")
        print()

car1 = Car("Mersedes", 2023, "Черный", 5000000, True)
car2 = FreightCar("Scania", 2020, "Белый", 7999999.99, True, 10)
car3 = Car("Nissan", 2021, "Красный", 2568000.00)

car1.car_info()
car1.set_price(333333.99)
car1.car_info()

car2.car_info()
car2.set_for_sale(False)
car2.car_info()

# car3.car_info()


set_cars = [car1, car2, car3]
# set_cars.append(Car.add_car())  #Добавить авто в магазин

for i in set_cars:
    i.car_info()

# Car.change_adres("В соседнем дворе")
#
# set_cars = [car1, car2, car3]
# for i in set_cars:
#     i.car_info()