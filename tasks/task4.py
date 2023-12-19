import random
import time
from abc import ABC, abstractmethod

import main


class Human(ABC):
    def __init__(self, fullname):
        self.fullname = fullname

    @abstractmethod
    def print(self):
        pass


class Employee(Human):
    def __init__(self, fullname, post):
        super().__init__(fullname)
        self.post = post

    def print(self):
        print(f'family: {self.fullname.split()[0]}, past: {self.post}')


class Visitor(Human):
    def __init__(self, fullname, age):
        super().__init__(fullname)
        self.age = age

    def print(self):
        print(f'name: {self.fullname.split()[1]}, age: {self.age}')


def random_post():
    posts = ["fireman", "manager", "organizer", "lead", "consultant", "teacher"]
    return posts[random.randint(0, len(posts) - 1)]


def random_name():
    names = ["Abraham", "Ada", "Benjamin", "Cecilia", "David", "Emily", "Francis", "Grace", "Henry", "Jane"]
    return names[random.randint(0, len(names) - 1)]


def random_family():
    families = ["Smith", "Jones", "Williams", "Brown", "Taylor", "Davies", "Wilson", "Evans", "Thomas", "Johnson"]
    return families[random.randint(0, len(families) - 1)]


def run():
    full_names = [" ".join([random_name(), random_family()]) for _ in range(5, 8)]
    humans = [Employee(fullname, random_post()) if random.randint(0, 1) else Visitor(fullname, random.randint(14, 90))
              for fullname in full_names]
    main.clear()
    print('Task 4', end='\r\n\r\n')
    time.sleep(0.3)
    print('Humans:')
    for human in humans:
        human.print()
        time.sleep(0.4)
    print()
    main.reverse_report()
