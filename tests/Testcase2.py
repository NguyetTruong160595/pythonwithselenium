import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from pages.login_page import *

user = "nguyettruongminh2@gmail.com"
wrong_passwd = "12345"
user_field = "//input[@id='login-username']"
continue_button = "//button[text()='Continue']"
pass_field = "//input[@id='login-password']"
login_button = "//button[@id='btn-login ']"

try:
    print("Testcase2: Verify user can not login if user enter wrong username or password when logging in Safetrust web portal")
    print("Staring test script")
    open_web()

    print("Entering username field with value" + user)
    driver.find_element_by_xpath(user_field).send_keys(user)
    time.sleep(3)

    print("Pressing Continue button")
    driver.find_element_by_xpath(continue_button).send_keys(Keys.ENTER)
    time.sleep(3)

    print("Entering wrong_passwd with value" + wrong_passwd)
    driver.find_element_by_xpath(pass_field).send_keys(wrong_passwd)
    time.sleep(3)

    print("Pressing Login button")
    driver.find_element_by_xpath(login_button).send_keys(Keys.ENTER)
    time.sleep(3)

    print("Checking login button is still display because login failed")
    driver.find_element_by_xpath(login_button).is_displayed()

    close_web()

    print("Test case successfully completed")

except Exception as e:
    print(e)

