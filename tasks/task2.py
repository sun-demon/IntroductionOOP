from abc import ABC, abstractmethod
from threading import Thread
import random
import time

import main


class FontColor:
    BLACK = '\x1B[30m'
    RED = '\x1B[31m'
    GREEN = '\x1B[32m'
    YELLOW = '\x1B[33m'
    BLUE = '\x1B[34m'
    MAGENTA = '\x1B[35m'
    CYAN = '\x1B[36m'
    WHITE = '\x1B[37m'
    BRIGHT_BLACK = '\x1B[90m'
    BRIGHT_RED = '\x1B[91m'
    BRIGHT_GREEN = '\x1B[92m'
    BRIGHT_YELLOW = '\x1B[93m'
    BRIGHT_BLUE = '\x1B[m94'
    BRIGHT_MAGENTA = '\x1B[95m'
    BRIGHT_CYAN = '\x1B[96m'
    BRIGHT_WHITE = '\x1B[97m'
    END = '\033[0m'


class Action(ABC):
    @abstractmethod
    def run(self, running_ground):
        pass

    @abstractmethod
    def swim(self, place):
        pass

    @abstractmethod
    def jump(self, water_space):
        pass


class Person(Action):
    def __init__(self, power):
        self.power = power

    def run(self, running_ground):
        running_ground.append(self)

    def swim(self, water_space):
        water_space.append(self)

    def jump(self, surface):
        surface.append(self)


class SimplePerson(Person):
    def __init__(self):
        super().__init__(3)


class HardPerson(Person):
    def __init__(self):
        super().__init__(5)


class Place(object):
    def __init__(self, symbol, length, density):
        self.symbol = symbol
        self.length = length
        self.density = density
        self.persons = []
        self.coords = []

    def append(self, person):
        self.persons.append(person)
        self.coords.append(0)

    def __run(self):
        while min(*self.coords) < self.length:
            for i in range(len(self.persons)):
                rand = (random.random() * 0.4 + 0.8)  # from 0.8 to 1.2
                new_coord = self.coords[i] + self.persons[i].power / self.density * rand
                self.coords[i] = min(self.length, new_coord)
            time.sleep(0.5)

    def run(self):
        self.coords = [0] * len(self.persons)
        thread = Thread(target=self.__run)
        thread.start()

    def print(self):
        for i in range(len(self.persons)):
            coord = int(self.coords[i])
            if coord == 0:
                print(self.symbol * self.length)
            else:
                color = FontColor.GREEN if isinstance(self.persons[i], SimplePerson) else FontColor.RED
                print(self.symbol * (coord - 1), end='')
                print(color + '#', end=FontColor.END)
                print(self.symbol * (self.length - coord))

    def is_completed(self):
        return min(self.coords) >= self.length


class Stadium(Place):
    def __init__(self):
        super().__init__('_', 50, 1)


class SwimmingPool(Place):
    def __init__(self):
        super().__init__('~', 30, 2)


class Trampoline(Place):
    def __init__(self):
        super().__init__(' ', 15, 3)


def __print(places):
    main.clear()
    print('Task 2', end='\r\n\r\n')
    for place in places:
        place.print()
        print()
    time.sleep(0.1)


def run():
    stadium, swimming_pool, trampoline = Stadium(), SwimmingPool(), Trampoline()
    places = [stadium, swimming_pool, trampoline]
    persons = [SimplePerson() if random.randint(0, 1) else HardPerson() for _ in range(random.randint(3, 9))]
    for person in persons:
        person.run(stadium)
        person.swim(swimming_pool)
        person.jump(trampoline)
    for place in places:
        place.run()
    while not all([place.is_completed() for place in places]):
        __print(places)
    else:
        __print(places)
    main.reverse_report()
