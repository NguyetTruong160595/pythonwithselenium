import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from pages.login_page import *

wrong_user = "nguyettruongminh2"
user_field = "//input[@id='login-username']"
disable_continue_button = "//button[text()='Continue' and @disabled='disabled']"

try:
    print("Testcase3: Verify Continue button will hidden if user enter wrong username format")
    print("Staring test script")
    open_web()

    print("Entering wrong username with value" + wrong_user)
    driver.find_element_by_xpath(user_field).send_keys(wrong_user)
    time.sleep(3)

    print("Checking continue button is hidden because username filed which enter wrong format")
    driver.find_element_by_xpath(disable_continue_button).is_displayed()
    time.sleep(3)

    close_web()

    print("Test case successfully completed")

except Exception as e:
    print(e)

