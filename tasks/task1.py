from random import randint
from abc import ABC, abstractmethod
import time

import main


class Parent(ABC):
    def __init__(self, grow):
        self.grow = grow

    def color_eye(self):
        return 'green'

    @abstractmethod
    def change_grow(self):
        pass

    def print_grow(self, end='\r\n'):
        print(f'grow: {self.grow}', end=end)


class Masha(Parent):
    def __init__(self):
        super().__init__(19)

    def color_eye(self):
        return 'brown'

    def change_grow(self):
        self.grow += randint(1, 2)


class Peter(Parent):
    def __init__(self):
        super().__init__(20)

    def change_grow(self):
        self.grow += randint(2, 3)


def run():
    main.clear()
    print('Task 1', end='\r\n\r\n')
    humans = [Masha() if randint(0, 1) else Peter() for _ in range(randint(2, 8))]
    for human in humans:
        print('Masha' if isinstance(human, Masha) else 'Peter', end=': ')
        human.print_grow(end=', ')
        print('eye color:', human.color_eye(), end=', ')
        print('changed ', end='')
        human.change_grow()
        human.print_grow()
        time.sleep(0.3)
    print('', end='\r\n\r\n')
    main.reverse_report()
