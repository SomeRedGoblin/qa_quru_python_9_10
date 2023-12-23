from selene import browser, have, be
import os


def test_complete_todo():
    browser.open('/automation-practice-form')

    # заполнение формы
    registration_form = browser.element('#userForm')
    registration_form.element('#firstName').should(be.blank).type('John')
    registration_form.element('#lastName').should(be.blank).type('Week')
    registration_form.element('#userEmail').should(be.blank).type('john.week@example.com')
    registration_form.all('#genterWrapper label').element_by(have.text("Male")).click()
    registration_form.element('#userNumber').should(be.blank).type('9123456789')
    registration_form.element('#dateOfBirthInput').click()
    registration_form.element('.react-datepicker__month-dropdown-container--select').click()
    registration_form.all('.react-datepicker__month-select > option').element_by(have.text("May")).click()
    registration_form.element('.react-datepicker__year-dropdown-container--select').click()
    registration_form.all('.react-datepicker__year-select > option').element_by(have.text("2000")).click()
    registration_form.all('.react-datepicker__day').element_by(have.text("4")).click()
    registration_form.element('#subjectsContainer').element('.subjects-auto-complete__value-container').click()
    registration_form.element('.subjects-auto-complete__input input').set_value('Math').press_enter()
    registration_form.element('#hobbiesWrapper').element('//*[text()=("Sports")]').click()
    registration_form.element('#hobbiesWrapper').element('//*[text()=("Music")]').click()
    registration_form.element('#uploadPicture').send_keys(os.path.abspath('data/test01.png'))
    registration_form.element('#currentAddress').type('ул. Ленина 4')
    registration_form.element('#state').click().element('#react-select-3-option-2').click()
    registration_form.all('#state').first().click()
    registration_form.element('#city').click().element('#react-select-4-option-1').click()
    registration_form.all('#submit').first().submit()

    # Проверка отправленных значений
    result_form = browser.element('.modal-content')
    result_form.element("//*[text()=('Student Name')]/../td[2]").should(have.text('John Week'))
    result_form.element("//*[text()=('Student Email')]/../td[2]").should(have.text('john.week@example.com'))
    result_form.element("//*[text()=('Gender')]/../td[2]").should(have.text('Male'))
    result_form.element("//*[text()=('Mobile')]/../td[2]").should(have.text('9123456789'))
    result_form.element("//*[text()=('Date of Birth')]/../td[2]").should(have.text('04 May,2000'))
    result_form.element("//*[text()=('Subjects')]/../td[2]").should(have.text('Maths'))
    result_form.element("//*[text()=('Hobbies')]/../td[2]").should(have.text('Sports, Music'))
    result_form.element("//*[text()=('Picture')]/../td[2]").should(have.text('test01.png'))
    result_form.element("//*[text()=('Address')]/../td[2]").should(have.text('ул. Ленина 4'))
    result_form.element("//*[text()=('State and City')]/../td[2]").should(have.text('Haryana Panipat'))
