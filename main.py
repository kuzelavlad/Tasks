def div(a: int, b: int) -> float:
    res = a / b
    print(res)
    return res


while True:
    try:
        a = float(input("First: "))
        b = float(input("Second: "))
        div(a, b)
    except (ValueError, ) as err:
        print(err)
    except ZeroDivisionError:
        print("Был введен ноль. Ошибка")


# выявление ошибок и пропуск их при необходимости




temp = []

def func() -> int :
    try:
        a = int(input("Введите число: \n"))
        temp.append(a)
        print(a)
    except ValueError:
        print("Неверные данные")


func()
# написал функцию, которая добавляет в список числа , если не числа - падает ошибка


temp = [1, 2, 3, 4]

def func():
    count = 0
    while count <3 :
        count +=1

        try:
            a = int(input("Enter index: \n"))
            print(temp[a])
        except IndexError:
             print("Введен неверный индекс")
        except ValueError:
            print("Неверное значение")
func()

# функия, которая в готовом списке выдает значение по индексу

temp_1 = [{
    "amount": "0.0082",
    "transactionFee": "0.0016",
    "coin": "ETH",
    "address": "0xFakeAddress",
    "applyTime": "2000-01-01 21:12:52",
    "network": "ETH",
},
{
    "amount": "0.00044",
    "transactionFee": "0.00044",
    "address": "0xFakeAddress",
    "applyTime": "2000-01-01 22:12:52",
}]

def sum_1():
    while True:
        try:
            a = int(input("Enter index: \n"))
            dict_1 = temp_1[a]
        except IndexError:
             print("Введен неверный индекс")
        except ValueError:
                print("Неверное значение")
        else:
            dict_1 = temp_1[a]
            print(float(dict_1["amount"]) - float(dict_1["transactionFee"]))
sum_1()

# достаем значение из дикта и вычитаем комиссию способ 1
def foo():
    try:
        idx = int(input("Введите номер транзакции: "))
        transaction = temp[idx]
    except (ValueError, IndexError) as err:
        print(err)
    else:
        print(float(transaction["amount"]) - float(transaction["transactionFee"]))

foo()

# способ 2



class Human:


    def __init__(self, name, salary, exp, job):

        self.name = name
        self.salary = salary
        self.exp = exp
        self.job = job


    def print_info(self):

        print(f"{self.name}. Salary is {self.salary} $. Jobs title is {self.job}. Stage is {self.exp}. Bonus: {getattr(self, 'bonus',  0)}")

    def func(self):
        self.exp += 1
        self.salary = float(self.salary) * 1.1

    def promotion(self, bonus: int):
        self.bonus = bonus


vlad = Human("Vlad", 3000 , 6, "director")

vlad.print_info()
vlad.promotion(23214)
vlad.print_info()
vlad.func()
vlad.print_info()




# Задача 1, классная работа
ordering_list = [{"name": "Meat", "price": 10},
                 {"name": "Chicken", "price": 23},
                 {"name": "Fish", "price": 12414},
                 {"name": "Solt", "price": 12415}]

print(max(ordering_list, key=lambda prod: prod["price"]))
# есть список покупок. надо найти самый дорогой

# Задача 2, классная работа


from __future__ import annotations  #все что есть в классе можно испольщорвтаь в аннотациях

class Product:
    def __init__(self, name: str, price: int, qty: int) -> None:
        self.name = name
        self.price = price
        self.qty = qty  # количество

    def __repr__(self) -> str: #делает красивый вид добавления
        return f"{self.name} -> qty: {self.qty}"

    @classmethod
    def make_banana(cls, qty: int):
        qty = 1
        return cls("Banana", 5, qty)

    @classmethod
    def make_beef(cls, qty: int):
        qty = 1
        return cls("Beef", 23, qty)
    @classmethod
    def make_water(cls, qty: int):
        qty = 1
        return cls("Water", 2, qty)
    @classmethod
    def make_water_2(cls, qty: int):
        qty = 1
        return cls("Water_2", 2, qty)

    @property
    def total_price(self) -> int:
        return self.qty * self.price





class Bucket:
    __id = 1     #глобальный классовый атрибут, чтобы каждая корзина была уникальгный

    def __init__(self):
        self.id = self.__id
        self.increment_id()
        self.products = []

    @classmethod #метод,который работает напрямую с классом
    def increment_id(cls) -> None: #увеличивает айдишник класса
        cls.__id += 1

    def add(self, product: Product):
        """Add product to bucket."""
        self.products.append(product)
        print(f"{product.name} was added")

    def remove(self, product: Product):
        """Remove product from bucket."""
        self.products.remove(product)
        print(f"{product.name} was removed")

    @property
    def total_price(self) -> int:
        total = 0
        for item in self.products:
            total += item.total_price
        return total


banana = Product("Banana", 5, 3)
beef = Product("Beef", 23, 1)
water = Product("Water", 2, 5)

bucket = Bucket() # создаем корзину, чтобы в нее потом полоджить продукты

bucket.add(banana)
bucket.add(beef)
bucket.add(water)

print(bucket.products)
print(bucket.total_price)
water_2 = Product("Water 2", 2, 3)

bucket.add(water_2)
print(bucket.total_price)
bucket.remove(water_2)
print(bucket.total_price)


# Задача 3

from __future__ import annotations
from datetime import datetime


class SpeedWarning(Exception):
    pass


class Cars:

    def __init__(self, model,year, price, color):
        self.model = model
        self.price = price
        self.color = color
        self.year = year
        self.speed = 0

    @classmethod
    def make_mb(cls):
        return cls("CLA 45 AMG", 2014, 27500, "black")
    @classmethod
    def make_bmw(cls):
        return cls("BMW M8", 2022, 159000, "white")

    @property
    def car_price(self) -> float:

        return self.price - self.price * ((datetime.now().year - self.year) * 5) / 100


    def __str__(self) -> str:
        return f"{self.car_price}"

    def car_speed(self):
        self.speed += 300

    def car_slow(self):
        if self.speed >= 100:
            raise SpeedWarning
        self.speed = 10

Cars.make_mb()
print(Cars.make_mb())
Mercedes = Cars.make_mb()
print(Mercedes)
print(Mercedes.price)
print(Mercedes.car_speed())
print(Mercedes.car_slow())



# Задача 4,


from enum import Enum # варианты которые могут быть


class TransportType(Enum):
    airplane = 0
    train = 1
    car = 2


class Transport:

    def __init__(self, wheels, seats, color, year):

        self.wheels = wheels
        self.seats = seats
        self.color = color
        self.year = year

    def move(self):
        raise NotImplementedError

    def charge(self):
        raise NotImplementedError

    def make_sound(self):
        raise NotImplementedError


class Airplane(Transport):
    type = TransportType.airplane
    def __init__(self,*args, name: str, fly_distance: int):
        super().__init__(*args)
        self.name = name
        self.fly_distance = fly_distance


    def move(self):
        print("I'm FLY")
    def charge(self):
        print("Меня норм заправили")

    def make_sound(self):
        print("ВИУ")
    def __repr__(self):
        return f'Количество колес:{self.wheels} \nКоличество мест: {self.seats} \nЦвет:{self.color} \nГод:{self.year} \nПозывной:{self.name} \nМаксимальная дистанция:{self.fly_distance}'


class Train(Transport):
    type = TransportType.train
    def __init__(self,*args, vagons, max_speed, qty_personal):
        super().__init__(*args)
        self.vagons = vagons
        self.max_speed = max_speed
        self.qty_personal = qty_personal

    def move(self):
        print("I'm run")

    def charge(self):
        print("В меня норм закинули угля")

    def make_sound(self):
        print("ВЖУХ")

    def __repr__(self):
        return f'Количество колес:{self.wheels} \nКоличество мест: {self.seats} \nЦвет:{self.color} \nГод:{self.year} \nКоличество вагонов:{self.vagons} \nМаксимальная cкорость:{self.max_speed}"км\ч" \nКоличество персонала:{self.qty_personal}'


class Car(Transport):
    type = TransportType.car
    def __init__(self, *args, max_speed_car, model):
        super().__init__(*args)
        self.max_speed_car = max_speed_car
        self.model = model

    def move(self):
        print("I'm drive")

    def charge(self):
        print("Только 98-бензин")

    def make_sound(self):
        print("Би-бип")

    def __repr__(self):
        return f'Количество колес:{self.wheels} \nКоличество мест: {self.seats} \nЦвет:{self.color} \nГод:{self.year} \nМаксимальная скорость:{self.max_speed_car} \nМодель:{self.model}'



obj = Airplane(4, 850, "white", 1988,name="Tata", fly_distance=1000)
obj_1 = Train(123414, 655, "grey", 1966, vagons= 88, max_speed = 100, qty_personal =55)
obj_2 = Car(4, 5, "Black", 2022, max_speed_car= 330, model= "MB CLA 45S")
print(obj)









