# This is a sample Python script.
from selenium import webdriver # type: ignore
import time

driver = webdriver.Chrome()

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def login(username, password):

    print("Clearing text in username field if exist")
    driver.find_element_by_xpath("//input[@id='login-username']").clear()
    print("Entering username " + username + " to username filed")
    driver.find_element_by_xpath("//input[@id='login-username']").send_keys(username)
    time.sleep(3)

    print("Pressing Continue button")
    driver.find_element_by_xpath("//button[text()='Continue']").send_keys(Keys.ENTER)
    time.sleep(3)

    print("Entering password " + password + " to password field")
    driver.find_element_by_xpath("//input[@id='login-password']").send_keys(password)
    time.sleep(3)

    print("Pressing Login button")
    driver.find_element_by_xpath("//button[@id='btn-login ']").click()
    time.sleep(5)

    print("Checking account icon is displayed to complete login process")
    driver.find_element_by_xpath("//span[text()='My Account']").is_displayed()


def logout():

    print("Pressing User icon to show the log out option")
    driver.find_element_by_xpath("//a[@id='userLink' and @class='dropdown-toggle']").click()
    time.sleep(3)

    print("Choosing Logout option")
    driver.find_element_by_xpath("//a[@id='LOGOUT']").click()
    time.sleep(3)

    print("Verify username field is displayed to complete logout process")
    user_textfield = EC.presence_of_element_located((By.ID, "login-username"))
    WebDriverWait(driver, 30).until(user_textfield)
    driver.find_element_by_xpath("//input[@id='login-username']").is_displayed()


def open_web():

    print("Access Safetrust web portal")
    driver.get("https://demo.safetrust.com/")
    time.sleep(10)

    print("Verify username field is displayed to complete open web process")
    driver.find_element_by_xpath("//input[@id='login-username']").is_displayed()


def close_web():
    print("Closing web portal after completing Test script")
    driver.close()


