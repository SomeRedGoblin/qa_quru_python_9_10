import dataclasses
from datetime import datetime
from enum import Enum

Hobbies = Enum("Hobbies", 'Sports Reading Music')


@dataclasses.dataclass
class User:
    full_name: str
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile: int
    birthday: datetime.date
    subjects: list
    hobbies: list[Hobbies]
    picture: str
    current_address: str
    state: str
    city: str


student = User(full_name='John Week', first_name='John', last_name='Week', email='john.week@example.com', gender='Male',
               mobile=9123456789, birthday=datetime(2000, 5, 4), subjects=['Maths'],
               hobbies=[Hobbies.Reading, Hobbies.Music],
               picture='test01.png', current_address='ул. Ленина 4', state='Haryana', city='Panipat')
