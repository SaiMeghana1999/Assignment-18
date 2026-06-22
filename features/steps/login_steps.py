from behave import *
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

from utils.config import *

import time


@given('User opens Zen Portal')
def open_portal(context):
    context.driver.get(URL)

    context.login = LoginPage(
        context.driver
    )


@then('Username textbox should be visible')
def validate_username(context):
    assert context.login.validate_email_box()


@then('Password textbox should be visible')
def validate_password(context):
    assert context.login.validate_password_box()


@then('Sign In button should be visible')
def validate_signin(context):
    assert context.login.validate_signin_button()


@when('User enters valid credentials')
def valid_login(context):
    context.login.login(
        VALID_EMAIL,
        VALID_PASSWORD
    )

    time.sleep(8)

    context.login.close_dashboard_popups()


@then('Login should be successful')
def success(context):
    assert "dashboard" in \
           context.driver.current_url


@when('User enters invalid credentials')
def invalid_login(context):
    context.login.login(
        INVALID_EMAIL,
        INVALID_PASSWORD
    )

    time.sleep(5)


@then('Login should fail')
def failure(context):
    assert "login" in \
           context.driver.current_url


@when('User logs in')
def login_logout(context):
    context.login.login(
        VALID_EMAIL,
        VALID_PASSWORD
    )

    time.sleep(8)

    context.login.close_dashboard_popups()


@then('User should logout successfully')
def logout(context):
    dashboard = DashboardPage(
        context.driver
    )

    dashboard.logout()

    time.sleep(5)

    assert "login" in \
           context.driver.current_url
