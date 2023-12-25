from selene import browser, have


class LeftPanel:

    def __init__(self):
        self.panel = browser.element('.left-pannel')

    def open(self, menu: str, sub_menu: str):
        browser.open('/')
        browser.all('.card-body').element_by(have.exact_text(menu)).click()
        browser.all('.menu-list span').element_by(have.exact_text(sub_menu)).click()
        # browser.all('.custom-checkbox').element_by(have.exact_text('Reading')).click()

    def open_simple_registration_form(self):
        self.open('Elements', 'Text Box')
