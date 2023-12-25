from selene import browser, have

from data import users
from model.application import app
from model.pages.simple_user_registration_page import SimpleUserRegistrationPage


def test_simple_registration():
    new_student = users.student

    registration_page = SimpleUserRegistrationPage()

    registration_page.open()
    registration_page.register(new_student)
    registration_page.should_have_registered(new_student)


def test_simple_registration_with_navigation_via_left_menu():
    new_student = users.student

    app.left_panel.open_simple_registration_form()

    app.simple_registration_page.register(new_student)
    app.simple_registration_page.should_have_registered(new_student)
