from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
driver = webdriver.Chrome('/usr/local/bin/chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/xhtml')
search_box = driver.find_element_by_name('q')
search_box.send_keys('seleniumhq')
search_box.submit()
time.sleep(2)
try:
    clickme = driver.find_element_by_xpath("//a[contains(@href,'http://seleniumhq.org')]")
except NoSuchElementException:
    assert 0, "can't find seleniumhq"
clickme.click()
time.sleep(5)  # Let the user actually see something!
driver.quit()
