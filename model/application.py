from model.pages.left_panel import LeftPanel
from model.pages.registration_page import RegistrationPage
from model.pages.simple_user_registration_page import SimpleUserRegistrationPage


class Application:
    def __init__(self):
        self.simple_registration_page = SimpleUserRegistrationPage()
        self.registration_page = RegistrationPage()
        self.left_panel = LeftPanel()


app = Application()
