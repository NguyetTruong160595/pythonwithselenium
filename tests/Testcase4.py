import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from pages.login_page import *

user = "nguyettruongminh22@gmail.com"
user_field = "//input[@id='login-username']"
continue_button = "//button[text()='Continue']"
disable_continue_button = "//button[text()='Continue' and @disabled='disabled']"
pass_field = "//input[@id='login-password']"
disable_login_button = "//button[@id='btn-login ' and @disabled='disabled']"


try:
    print("Testcase4: Verify user can not press Continue/Login button if username/password filed is blank")
    print("Staring test script")
    open_web()

    print("Checking username field is displayed and keeping it blank")
    driver.find_element_by_xpath(user_field).is_displayed()
    time.sleep(3)

    print("Checking Continue button is hidden because username field is blank")
    driver.find_element_by_xpath(disable_continue_button).is_displayed()
    time.sleep(3)

    print("Entering valid username with value" + user + " to check Login button when keeping password filed is blank")
    driver.find_element_by_xpath(user_field).send_keys(user)
    time.sleep(3)

    print("Pressing Continue button")
    driver.find_element_by_xpath(continue_button).send_keys(Keys.ENTER)
    time.sleep(3)

    print("Checking password field is displayed")
    driver.find_element_by_xpath(pass_field).is_displayed()
    time.sleep(3)

    print("Checking Login button is hidden when password field is blank")
    driver.find_element_by_xpath(disable_login_button).is_displayed()
    time.sleep(3)

    close_web()

    print("Test case successfully completed")

except Exception as e:
    print(e)
