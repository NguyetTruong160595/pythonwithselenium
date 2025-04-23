import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from pages.login_page import *

user = "nguyettruongminh2@gmail.com"
passwd = "12345x@X"


try:
    print("Testcase6: Verify user can logout and re-login with the same account multiple times successfully")
    print("Staring test script")
    open_web()

    i = 0
    for i in range(5):
        print("Loop number " + str(i))

        login(user, passwd)

        logout()

    close_web()
    print("Test case successfully completed")

except Exception as e:
    print(e)
