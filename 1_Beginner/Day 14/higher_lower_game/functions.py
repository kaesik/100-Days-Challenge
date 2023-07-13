import random
from data import *


def fun_random_person():
    """Picks random person from data"""
    random_person = random.choice(data)
    return random_person


def fun_person_data(person):
    """Gets data of random person"""
    person_data_list = list(person.items())
    person_name = person_data_list[0][1]
    person_followers = person_data_list[1][1]
    person_description = person_data_list[2][1]
    person_country = person_data_list[3][1]
    return person_name, person_followers, person_description, person_country


def fun_win_round(person_1, person_2):
    """True if you win the round"""
    if person_1 > person_2:
        return True
