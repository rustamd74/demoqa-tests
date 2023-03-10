from selene import command
from selene.support.conditions import be, have
from selene.support.shared import browser

from demoqa_tests.model.controls import radio_button, date_picker, checkbox, dropdown
from demoqa_tests.utils import file_path


def open_page():
    browser.open('/automation-practice-form')
    ads = browser.all('[id^=google_ads_][id$=container__]')
    if ads.wait.until(have.size_greater_than_or_equal(3)):
        ads.perform(command.js.remove)


def submit_data(first_name, last_name, email, user_number, current_address):
    browser.element('#firstName').should(be.blank).type(first_name)
    browser.element('#lastName').should(be.blank).type(last_name)
    browser.element('#userEmail').should(be.blank).type(email)
    browser.element('#userNumber').should(be.blank).type(user_number)
    browser.element('#currentAddress').should(be.blank).type(current_address)


def select_gender(gender):
    radio_button.select_value(browser.all('#gender-radio-1'), gender)


def date_birthday(*, day, month, year):
    browser.element('#dateOfBirthInput').click()
    date_picker.select_date(month, year, day)


def subject(texts):
    browser.element('#subjectsInput').type(texts).press_enter()


def set_hobbies(texts):
    browser.element('[for="hobbies-checkbox-3"]').perform(command.js.scroll_into_view)
    checkbox.select_hobbies(browser.all('[for^=hobbies-checkbox]'), texts)


def insert_picture(path_to_picture):
    file_path.create_path('#uploadPicture', path_to_picture)


def select_state(value):
    dropdown.select('#state', value)


def select_city(value):
    dropdown.select('#city', value)


def submit():
    browser.element('#submit').press_enter()


def assert_registration_student(*args):
    browser.element('.table').all('td').even.should(have.exact_texts(args))
