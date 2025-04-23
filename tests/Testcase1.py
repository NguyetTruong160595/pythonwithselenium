import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from pages.login_page import *

user = "nguyettruongminh2@gmail.com"
passwd = "12345x@X"

try:
    print("Testcase1: Verify user can login successfully with valid username and password")
    print("Staring test script")
    open_web()

    print("Logging in with account" + user)
    login(user, passwd)

    close_web()

    print("Test case successfully completed")

except Exception as e:
    print(e)
