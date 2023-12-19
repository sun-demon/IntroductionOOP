import itertools
import random
import time

import main


class Holiday(object):
    def __init__(self, name, invited, max_persons):
        self.name = name
        self.invited = invited
        self.families = []
        self.max_persons = max_persons

    def add_family(self, family):
        if family.name not in self.invited:
            raise Exception(f'The family \'{family.name}\' isn\'t invited')
        n_persons = sum([family.n_persons for family in self.families])
        if (n_persons + family.n_persons) > self.max_persons:
            free_places = self.max_persons - n_persons
            raise Exception(f'The family \'{family.name}\' can\'t be added: count persons in family: {family.n_persons}, free places: {free_places} ')
        self.families.append(family)


class Family(object):
    def __init__(self, name, n_persons):
        self.name = name
        self.n_persons = n_persons


def run():
    names_families = ["Smith", "Jones", "Williams", "Brown", "Taylor", "Davies", "Wilson", "Evans", "Thomas", "Johnson"]
    families = [Family(name, random.randint(2, 5)) for name in names_families]
    holiday_invited = [name for name in names_families if random.randint(0, 1)]
    holiday_max_persons = len(holiday_invited) * 3
    holiday = Holiday("Halloween", holiday_invited, holiday_max_persons)
    main.clear()
    print('Task 3', end='\r\n\r\n')
    time.sleep(0.7)
    print(f'The holiday: {holiday.name}')
    time.sleep(0.7)
    for family in families:
        try:
            holiday.add_family(family)
            print(f'The family {family.name} is successful added')
        except Exception as exception:
            for arg in exception.args:
                print(arg)
        time.sleep(0.3)
    print()
    main.reverse_report()
