import dataclasses
from datetime import datetime
from enum import Enum


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile: int
    birthday: datetime.date
    subjects: list
    # hobbies: Hobbies()
    hobbies: list
    img_name: str
    current_address: str
    state: str
    city: str


# class Hobbies(Enum):
#     Sports: str
#     Reading: str
#     Music: str

basic_user = User(first_name='John', last_name='Week', email='john.week@example.com', gender='Male',
                  mobile=9123456789, birthday='04 May 2000', subjects=['Maths'],
                  hobbies=['Sports, Music'],
                  img_name='test01.png', current_address='ул. Ленина 4', state='Haryana', city='Panipat')
