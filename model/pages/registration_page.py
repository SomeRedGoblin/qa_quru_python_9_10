import os

from selene import have, command
from selene import browser

from data.users import User


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.state = browser.element('#state')

    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        self.first_name.type(value)

    def fill_last_name(self, value):
        self.last_name.type(value)

    def fill_email(self, value):
        browser.element('#userEmail').type(value)

    def select_gender(self, value):
        browser.all('#genterWrapper label').element_by(have.text(value)).click()

    def fill_mobile(self, value):
        browser.element('#userNumber').type(value)

    def fill_date_of_birth(self, date):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-dropdown-container--select').click()
        browser.all('.react-datepicker__month-select > option').element_by(have.text(date.strftime('%b'))).click()
        browser.element('.react-datepicker__year-dropdown-container--select').click()
        browser.all('.react-datepicker__year-select > option').element_by(have.text(str(date.year))).click()
        browser.all('.react-datepicker__day').element_by(have.text(str(date.day))).click()

    def select_subjects(self, values):
        for value in values:
            browser.element('#subjectsContainer').element('.subjects-auto-complete__value-container').click()
            browser.element('.subjects-auto-complete__input input').set_value(value).press_enter()

    def select_hobbies(self, values):
        for value in values:
            browser.element('#hobbiesWrapper').element(f'//*[text()=("{value.name}")]').click()

    def select_picture(self, value):
        browser.element('#uploadPicture').send_keys(os.path.abspath(f'resources/{value}'))

    def fill_state(self, name):
        self.state.perform(command.js.scroll_into_view)
        self.state.click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(name)
        ).click()

    def fill_city(self, name):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(name)
        ).click()

    def fill_curent_address(self, value):
        browser.element('#currentAddress').type(value)

    def submit_form(self):
        browser.all('#submit').first().submit()

    def get_list_of_hobby_name(self, hobbies):
        return ', '.join(list(map(lambda n: n.name, hobbies)))

    def register(self, user: User):
        self.fill_first_name(user.first_name)
        self.fill_last_name(user.last_name)
        self.fill_email(user.email)
        self.select_gender(user.gender)
        self.fill_mobile(user.mobile)
        self.fill_date_of_birth(user.birthday)
        self.select_subjects(user.subjects)
        self.select_hobbies(user.hobbies)
        self.select_picture(user.picture)
        self.fill_curent_address(user.current_address)
        self.fill_state(user.state)
        self.fill_city(user.city)
        self.submit_form()

    def should_have_registered(self, user: User):

        browser.element('.table').all('td').even.should(
            have.exact_texts(
                user.first_name + ' ' + user.last_name,
                user.email,
                user.gender,
                str(user.mobile),
                user.birthday.strftime('%d %b,%Y'),
                user.subjects,
                self.get_list_of_hobby_name(user.hobbies),
                user.picture,
                user.current_address,
                user.state + ' ' + user.city
            )
        )
