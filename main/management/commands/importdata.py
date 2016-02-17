from pprint import pprint

import os
from django.core.management.base import BaseCommand, CommandError
from main.models import Person
from phones.settings import BASE_DIR


def parse_line(line):
    result = line.split("	")
    result = filter(None, result)

    if len(result) == 2:
        return {
            "name": "{0} {1}".format(result[0], result[1]),
            "phone_one": "",
            "phone_two": ""
        }
    elif len(result) == 3:
        return {
            "name": "{0} {1}".format(result[1], result[2]),
            "phone_one": "{0}".format(result[0]),
            "phone_two": ""
        }
    elif len(result) == 4:
        return {
            "name": "{0} {1}".format(result[2], result[3]),
            "phone_one": "{0}".format(result[0]),
            "phone_two": "{0}".format(result[1])
        }
    return None

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        f = open(os.path.join(BASE_DIR, 'data.txt'), 'r+')

        for line in f:
            line_dict = parse_line(line)
            if line_dict is not None:
                person = Person(name=line_dict['name'], phone_one=line_dict['phone_one'], phone_two=line_dict['phone_two'])
                person.save()