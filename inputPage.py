from tkinter import *



class get_Input:
    def __init__(self) -> None:
        self.home()
        
    def home(self):
        # create a GUI User window
        gui = Tk()
        self.user = StringVar()
        gui.configure(background="light blue")
        gui.title("E Commerce Website")
        gui.geometry("1800x800")
        frame = Frame(background="light green",relief='sunken')
        login_label = Label(frame, text="Login",background='light green', fg="#FFFFFF", font=("Arial", 30))
        username_label = Label(frame, text="Username", background='light green', fg="#FFFFFF", font=("Arial", 16))
        username_entry = Entry(frame, font=("Arial", 16),textvariable=self.user)
        login_button = Button(frame, text="Login",background='white', font=("Arial", 16), command=gui.withdraw)
        login_label.grid(row=0, column=0, columnspan=2, sticky="we", pady=40)
        username_label.grid(row=1, column=0,padx=5)
        username_entry.grid(row=1, column=1, pady=20, padx=5)
        login_button.grid(row=3, column=0, columnspan=2, pady=30)
        frame.place(relx=.5, rely=.5,anchor="c")
        gui.mainloop()
        self.login(self.user.get())

    def login(self,username):
        print("YAY",username)





i = get_Input()