from selene import browser, have, command

from data import resource


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

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-dropdown-container--select').click()
        browser.all('.react-datepicker__month-select > option').element_by(have.text(month)).click()
        browser.element('.react-datepicker__year-dropdown-container--select').click()
        browser.all('.react-datepicker__year-select > option').element_by(have.text(year)).click()
        browser.all('.react-datepicker__day').element_by(have.text(day)).click()

    def select_subjects(self, value):
        browser.element('#subjectsContainer').element('.subjects-auto-complete__value-container').click()
        browser.element('.subjects-auto-complete__input input').set_value(value).press_enter()

    def select_hobbies(self, value):
        browser.element('#hobbiesWrapper').element(f'//*[text()=("{value}")]').click()

    def select_picture(self, value):
        browser.element('#uploadPicture').send_keys(resource.path(value))

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

    def should_have_registered(self, full_name, email, gender, phone, birthday, subjects, hobbies, img_name,
                               current_address, state_and_city):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                phone,
                birthday,
                subjects,
                hobbies,
                img_name,
                current_address,
                state_and_city
            )
        )
