# Создать систему классов описывающих транспорт и животных.
# Методы и поля описать на свое усмотрение.
# У классов животных обязательно добавить метод say() который будет описывать звуки издаваемые животным.

# Kласс - транспорт, в нем есть : государственный номер, кол-во колес, мощность двигателя, максимальная скорость

class Transport:
    def __init__(self, gos_number, wheels, power_engine, speed):
        self.gos_number = gos_number
        self.wheels = wheels
        self.power_engine = power_engine
        self.speed = speed

# Класс - велосипед, в нем есть : скорость, кол-во колес, тип велосипеда (дорожный, городской, для гор)

class Bicycle(Transport):
    def __init__(self, speed, transport_type):
        # Класс Bicycle наследует от класса Transport скорость
        # Кол-во колес 2
        super().__init__(speed, 2)
        self.transport_type = transport_type

# Класс - автомобиль, в нем есть : государственный номер, скорость, кол-во колес,
# тип автомобиля (седан, универсал, хэтчбек, купе)

class Automobile(Transport):
    def __init__(self, gos_number, speed, transport_type):
        # Класс Automobile наследует от класса Transport государственный номер, скорость
        # Кол-во колес 4
        super().__init__(gos_number, speed, 4)
        self.transport_type = transport_type


# Класс - автобус, в нем есть : государственный  номер, кол-во колес, мощность двигателя, скорость,
# тип автобуса (обычный, школьный)

class Bus(Transport):
    def __init__(self, gos_number, wheels, power_engine, speed, type_bus):
        # Класс Bus наследует от класса Transport государственный номер, кол-во колес, мощность двигателя, скорость
        super().__init__(gos_number, wheels, power_engine, speed)
        self.type_bus = type_bus

# ---------------------------------------------------------------------------------------------------------------------

class Animal:
    def __init__(self, name, weight, speed):
        self.name = name
        self.weight = weight
        self.speed = speed

# Класс - Birds, в нем есть : название, вес, скорость передвижения, имеет ли способность летать

class Birds(Animal):
    def __init__(self, name, weight, speed, flying):
        # Класс Birds наследует от класса Animal:
        super().__init__(name, weight, speed)
        self.flying = flying


# Класс - Parrot : название, вес, скорость передвижения, имеет ли способность летать, продолжительность жизни, цвет


class Parrot(Birds):
    def __init__(self, name, weight, speed, flying, lifetime, color):
        # Класс Parrot наследует от класса Birds:
        super().__init__(name, weight, speed, flying)
        self.lifetime = lifetime
        self.color = color

    def say(self):
        print("Qaaaa")


# Класс - Crow : название, вес, скорость передвижения, имеет ли способность летать, размах крыльев

class Crow(Birds):
    def __init__(self, name, weight, speed, flying, wingspan):
        # Класс Crow наследует от класса Birds:
        super().__init__(name, weight, speed, flying)
        self.wingspan = wingspan

    def say(self):
        print("Carcarcar")


# Класс - Reptiles : название, вес, скорость передвижения, Размер, умение плавать

class Reptiles(Animal):
    def __init__(self, name, weight, speed, size, ability_to_swim):
        # Класс Reptiles наследует от класса Animal:
        super().__init__(name, weight, speed)
        self.size = size
        self.ability_to_swim = ability_to_swim

# Класс - Chameleon : название, вес, скорость передвижения, размер, умение плавать, способность менять окрас

class Chameleon(Reptiles):
    def __init__(self, name, weight, speed, size, ability_to_swim, ability_to_change_color):
        # Класс Chameleon наследует от класса Reptiles:
        super().__init__(name, weight, speed, size, ability_to_swim)
        self.ability_to_change_color = ability_to_change_color

    def say(self):
        print("Ssss")

# Класс - Crocodile : название, вес, скорость передвижения, размер, хищник или нет

class Crocodile(Reptiles):
    def __init__(self, name, weight, speed, size, raptor):
        # Класс Crocodile наследует от класса Reptiles:
        super().__init__(name, weight, speed, size)
        self.raptor = raptor

    def say(self):
        print("Rrrrrr")

# Класс - Mammals : название, вес, скорость передвижения, размер, хищник или нет

class Mammals(Animal):
    def __init__(self, name, weight, speed, raptor):
        # Класс Mammals наследует от класса Animal:
        super().__init__(name, weight, speed)
        self.raptor = raptor

# Класс - Lion : название, вес, скорость передвижения, размер, хищник или нет, окрас

class Lion(Mammals):
    def __init__(self, name, weight, speed, raptor, color):
        # Класс Lion наследует от класса Mammals:
        super().__init__(name, weight, speed, raptor)
        self.color = color

    def say(self):
        print("Rarrr")

# Класс - Cat : название, вес, скорость передвижения, порода, домашнее животное или нет


class Cat(Mammals):
    def __init__(self, name, weight, speed, breed, domestic_animal):
        # Класс Cat наследует от класса Mammals:
        super().__init__(name, weight, speed, breed)
        self.domestic_animal = domestic_animal

    def say(self):
        print("Meow")