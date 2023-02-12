from playwright.sync_api import Page, expect


class LoginPage:
    URL = ""

    def __init__(self, page: Page) -> None:
        self.page = page
        self.email = page.get_by_placeholder("Email")
        self.password = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Log In")
        self.admin_label = page.get_by_role("link", name="Adminarea")

    def login(self, email: str, password: str):
        self.email.fill(email)
        self.password.fill(password)
        self.login_button.click()
        expect(self.admin_label).to_be_visible()
        expect(self.admin_label).to_have_attribute("href", "/admins")

    def navigate(self):
        self.page.goto(self.URL)

    def login_user(self, customer_name: str):
        self.page.goto(
            f'{self.URL}/users?query={customer_name}&per_page=10&commit=Search')
