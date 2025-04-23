import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from pages.login_page import *

user = "nguyettruongminh1@gmail.com"
wrong_passwd = "12345"
user_field = "//input[@id='login-username']"
pass_field = "//input[@id='login-password']"
continue_button = "//button[text()='Continue']"
login_button = "//button[@id='btn-login ']"
block_message = "//h4[contains(text(),'Your session is blocked for')]"

try:
    print("Testcase5: Verify user session will block if user enter wrong username/password 5 times")
    print("Staring test script")
    open_web()

    print("Entering username field with value" + user)
    driver.find_element_by_xpath(user_field).send_keys(user)
    time.sleep(3)

    print("Pressing Continue button")
    driver.find_element_by_xpath(continue_button).send_keys(Keys.ENTER)
    time.sleep(3)

    i = 0
    for i in range(6):
        print("Loop number is " + str(i))

        print("Clearing text in password field if exist")
        driver.find_element_by_xpath(pass_field).clear()
        print("Entering wrong_passwd" + wrong_passwd + " to password filed")
        driver.find_element_by_xpath(pass_field).send_keys(wrong_passwd)
        time.sleep(3)

        print("Pressing Login button")
        driver.find_element_by_xpath(login_button).send_keys(Keys.ENTER)
        time.sleep(5)

        print("Checking login button still display because login failed")
        driver.find_element_by_xpath(login_button).is_displayed()
        time.sleep(5)

    print("Block account message is displayed because user enter wrong password 5 times")
    driver.find_element_by_xpath(block_message)

    close_web()

    print("Test case successfully completed")

except Exception as e:
    print(e)

