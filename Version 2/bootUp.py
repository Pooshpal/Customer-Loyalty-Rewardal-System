import threading
from UserPortal import userPortal
from RestFull_API import api
import customtkinter


def userPort():
    customtkinter.set_default_color_theme("blue")
    win = customtkinter.CTk()
    test_run = userPortal(win)
    win.mainloop()

def api_():
    test_run = api()


t1 = threading.Thread(target=userPort )
t2 = threading.Thread(target=api_)
 
# starting thread 1
t1.start()
# starting thread 2
t2.start()

print("Ending Thread!")