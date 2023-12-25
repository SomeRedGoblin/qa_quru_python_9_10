from selene import browser, have

from data.users import User


class SimpleUserRegistrationPage:
    def __init__(self):
        self.full_name = browser.element('#userName')
        self.email = browser.element('#userEmail')
        self.current_address = browser.element('#currentAddress')
        self.permanent_address = browser.element('#permanentAddress')
        self.submit = browser.element('#submit')

    def open(self):
        browser.open('/text-box')

    def register(self, user: User):
        self.full_name.type(user.first_name + ' ' + user.last_name)
        self.email.type(user.email)
        self.current_address.type(user.current_address)
        self.permanent_address.type(user.current_address + ' ' + user.state + ' ' + user.city)
        browser.element('#submit').click()

    def should_have_registered(self, user: User):
        browser.element('#output').element('#name').should(have.text(user.first_name + ' ' + user.last_name))
        browser.element('#output').element('#email').should(have.text(user.email))
        browser.element('#output').element('#currentAddress').should(have.text(user.current_address))
        browser.element('#output').element('#permanentAddress').should(
            have.text(user.current_address + ' ' + user.state + ' ' + user.city))
