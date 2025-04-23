from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def get_driver(browser="chrome"):
    if browser == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == "firefox":
        driver = webdriver.Firefox(GeckoDriverManager().install())
    driver.maximize_window()
    return driver