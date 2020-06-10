import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

## FAKE POP SCRIPT
import random
from ProTwo.models import User
from faker import faker

fakegen = Faker()

def populate(N=5):
    #Create fake data entry
    fake_Fname = fakegen.first_name()
    fake_Lname = fakegen.last_name()
    fake_email = fakegen.mail()


if __name__ == '__main__':
    print("populating script!")
    populate(10)
    print("populating complete!")
