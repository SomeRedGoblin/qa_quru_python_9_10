from data import users

from model.pages.simple_user_registration_page import SimpleUserRegistrationPage


def test_complete_todo():
    registration_page = SimpleUserRegistrationPage()

    # заполнение формы
    new_student = users.student

    registration_page.open()
    registration_page.register(new_student)
    registration_page.should_have_registered(new_student)
