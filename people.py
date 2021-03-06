#!/usr/bin/env python
"""people dictionary to showoff namedtuple"""
from collections import namedtuple
PERSON = namedtuple('person', 'first_name surname age pet hobbies')


def setup_people():
    """returns a dictionary of people with
       key firstname_surname: value: namedtuple PERSON
       that has firstname, surname, age, pet, hobbies items
    """
    people = {}
    _add_oliver(people)
    _add_eeyore(people)
    return people


def _add_oliver(people):
    """ adds oliver """
    new_p = PERSON(first_name='Oliver', surname='Smart',
                   age=21, pet='Rat', hobbies=[])
    key = new_p.first_name + '_' + new_p.surname
    people[key] = new_p

def _add_eeyore(people):
    """Adds eeyore"""
    new_p = PERSON(first_name='Eeyore', surname='Milne',
                    age=98, pet='', hobbies=['Being gloomy, eating thistles and sugar cubes, playing Poohsticks, going to birthday parties, flowers, stars, sad stories and poems, looking over his hill'])
    key = new_p.first_name + '_' + new_p.surname
    people[key] = new_p

def main():
    """ main function run as script """
    people = setup_people()
    print(people)


if __name__ == '__main__':
    main()
