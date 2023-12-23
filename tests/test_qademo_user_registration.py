from data import users

from model.pages.registration_page import RegistrationPage


def test_complete_todo():
    registration_page = RegistrationPage()

    # заполнение формы
    new_student = users.student
    registration_page.open()
    registration_page.register(new_student)
    registration_page.should_have_registered(new_student)
