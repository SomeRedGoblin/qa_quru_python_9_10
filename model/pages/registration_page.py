from selene import browser, have, command

from data import resources
from data.users import User


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.state = browser.element('#state')

    def open(self):
        browser.open('/automation-practice-form')

    def __fill_first_name(self, value):
        self.first_name.type(value)

    def __fill_last_name(self, value):
        self.last_name.type(value)

    def __fill_email(self, value):
        browser.element('#userEmail').type(value)

    def __select_gender(self, value):
        browser.all('#genterWrapper label').element_by(have.text(value)).click()

    def __fill_mobile(self, value):
        browser.element('#userNumber').type(value)

    def __fill_date_of_birth(self, date):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-dropdown-container--select').click()
        browser.all('.react-datepicker__month-select > option').element_by(have.text(date.strftime('%b'))).click()
        browser.element('.react-datepicker__year-dropdown-container--select').click()
        browser.all('.react-datepicker__year-select > option').element_by(have.text(str(date.year))).click()
        browser.all('.react-datepicker__day').element_by(have.text(str(date.day))).click()

    def __select_subjects(self, values):
        for value in values:
            browser.element('#subjectsContainer').element('.subjects-auto-complete__value-container').click()
            browser.element('.subjects-auto-complete__input input').set_value(value).press_enter()

    def __select_hobbies(self, values):
        for value in values:
            browser.element('#hobbiesWrapper').element(f'//*[text()=("{value.name}")]').click()

    def __select_picture(self, value):
        browser.element('#uploadPicture').send_keys(resources.path(value))

    def __fill_state(self, name):
        self.state.perform(command.js.scroll_into_view)
        self.state.click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(name)
        ).click()

    def __fill_city(self, name):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(name)
        ).click()

    def __fill_curent_address(self, value):
        browser.element('#currentAddress').type(value)

    def __submit_form(self):
        browser.all('#submit').first().submit()

    def __get_list_of_hobby_name(self, hobbies):
        return ', '.join(list(map(lambda n: n.name, hobbies)))

    def register(self, user: User):
        self.__fill_first_name(user.first_name)
        self.__fill_last_name(user.last_name)
        self.__fill_email(user.email)
        self.__select_gender(user.gender)
        self.__fill_mobile(user.mobile)
        self.__fill_date_of_birth(user.birthday)
        self.__select_subjects(user.subjects)
        self.__select_hobbies(user.hobbies)
        self.__select_picture(user.picture)
        self.__fill_curent_address(user.current_address)
        self.__fill_state(user.state)
        self.__fill_city(user.city)
        self.__submit_form()

    def should_have_registered(self, user: User):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                user.first_name + ' ' + user.last_name,
                user.email,
                user.gender,
                str(user.mobile),
                user.birthday.strftime('%d %b,%Y'),
                user.subjects,
                self.__get_list_of_hobby_name(user.hobbies),
                user.picture,
                user.current_address,
                user.state + ' ' + user.city
            )
        )
