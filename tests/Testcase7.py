import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from pages.login_page import *

user1 = "nguyettruongminh1@gmail.com"
passwd1 = "12345x@X"
user2 = "nguyettruongminh2@gmail.com"
passwd2 = "12345x@X"

try:
    print("Testcase7: Verify user can logout and re-login with the another account multiple times successfully.")
    print("Staring test script")
    open_web()

    i = 0
    for i in range(3):
        print("Loop " + str(i) + " Login with account " + user1)
        login(user1, passwd1)

        print("Loop " + str(i) + " Logout account " + user1)
        logout()

        print("Loop " + str(i) + " Login with account " + user2)
        login(user2, passwd2)

        print("Loop " + str(i) + " Logout account " + user2)
        logout()

    close_web()

    print("Test case successfully completed")

except Exception as e:
    print(e)

