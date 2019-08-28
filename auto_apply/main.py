"""
Applies to companies.
"""
from time import sleep

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from greenhouse import Greenhouse

# Options to run within Docker Container
# From: https://github.com/heroku/heroku-buildpack-google-chrome/issues/46
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
"""
url = 'http://www.python.org'
url = 'https://boards.greenhouse.io/flexport/jobs/1799287?s=LinkedIn&source=LinkedIn'

with WebDriver(Chrome(chrome_options=chrome_options)) as driver:
    driver.get(url)
    elem = driver.find_element_by_id('first_name')
    elem.clear()
    elem.send_keys("pycon")
    # elem.send_keys(Keys.RETURN)
    # assert "No results found." not in driver.page_source
    sleep(3)
"""


def main():
    url = 'https://boards.greenhouse.io/flexport/jobs/1799287?s=LinkedIn&source=LinkedIn'

    g = Greenhouse()

    g.get(url)

    for id, value in g.data.items():
        g.enter_field(id, value)

    g.enter_by_attribute('w', 'v')

    sleep(10000)

if __name__ == '__main__':
    main()
