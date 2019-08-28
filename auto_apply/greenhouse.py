"""Greenhouse Apply"""
from selenium.webdriver import Chrome

class Greenhouse:

    FIRST_NAME = 'first_name'
    LAST_NAME = 'last_name'
    EMAIL = 'email'
    PHONE = 'phone'

    def __init__(self):
        self.driver = Chrome()
        self.data = {
            'first_name': '',
            'last_name' : '',
            'email': '',
            'phone': ''
        }

    def get(self, url):
        self.driver.get(url)

    def enter_field(self, id, value):
        input_text = self.driver.find_element_by_id(id)
        input_text.send_keys(value)

    def enter_by_attribute(self, attribute, value):
        e = self.driver.find_element_by_css_selector("[autocomplete='custom-question-linkedin-profile']")
        e.send_keys('LinkedIN')