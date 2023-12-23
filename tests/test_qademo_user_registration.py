from selene import browser, have, be
import os
from model.pages.registration_page import RegistrationPage


def test_complete_todo():
    registration_page = RegistrationPage()
    registration_page.open()

    # заполнение формы

    registration_page.fill_first_name('John')
    registration_page.fill_last_name('Week')
    registration_page.fill_email('john.week@example.com')
    registration_page.select_gender("Male")
    registration_page.fill_mobile('9123456789')
    registration_page.fill_date_of_birth('2000', 'May', '4')
    registration_page.select_subjects('Math')
    registration_page.select_hobbies('Sports')
    registration_page.select_hobbies('Music')

    browser.element('#uploadPicture').send_keys(os.path.abspath('resources/test01.png'))
    browser.element('#currentAddress').type('ул. Ленина 4')

    registration_page.fill_state('Haryana')
    registration_page.fill_city('Panipat')

    browser.all('#submit').first().submit()

    # Проверка отправленных значений
    registration_page.should_registered_user_with(
        'John Week',
        'john.week@example.com',
        'Male',
        '9123456789',
        '04 May,2000',
        'Maths',
        'Sports, Music',
        'test01.png',
        'ул. Ленина 4',
        'Haryana Panipat',
    )

    # result_form = browser.element('.modal-content')
    # result_form.element("//*[text()=('Student Name')]/../td[2]").should(have.text('John Week'))
    # result_form.element("//*[text()=('Student Email')]/../td[2]").should(have.text('john.week@example.com'))
    # result_form.element("//*[text()=('Gender')]/../td[2]").should(have.text('Male'))
    # result_form.element("//*[text()=('Mobile')]/../td[2]").should(have.text('9123456789'))
    # result_form.element("//*[text()=('Date of Birth')]/../td[2]").should(have.text('04 May,2000'))
    # result_form.element("//*[text()=('Subjects')]/../td[2]").should(have.text('Maths'))
    # result_form.element("//*[text()=('Hobbies')]/../td[2]").should(have.text('Sports, Music'))
    # result_form.element("//*[text()=('Picture')]/../td[2]").should(have.text('test01.png'))
    # result_form.element("//*[text()=('Address')]/../td[2]").should(have.text('ул. Ленина 4'))
    # result_form.element("//*[text()=('State and City')]/../td[2]").should(have.text('Haryana Panipat'))
