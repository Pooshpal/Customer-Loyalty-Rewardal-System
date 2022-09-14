from tkinter import *
from Database import _database



class get_Input:
    def __init__(self) -> None:
        #connect to database
        self.db = _database()
        # create a GUI User window
        self.win = Tk()
        self.user = StringVar()
        self.win.configure(background="light blue")
        self.win.title("E Commerce Website")
        self.win.geometry("1800x800")
        self.userLoginFrame  = Frame(background="light green",relief='sunken')
        self.userDetailsFrame = Frame(background="light green",relief='sunken')
        self.userLoginFrame.place(relx=.5, rely=.5,anchor="c")
        self.userLoginPage()
        self.win.mainloop()

    def change_to_userLogin(self):
        for widget in self.userDetailsFrame.winfo_children():
            widget.destroy()
        self.userLoginFrame.place(relx=.5, rely=.5,anchor="c")
        self.userDetailsFrame.pack_forget()
        self.userLoginPage()

    def change_to_userDetails(self):
        self.userDetailsFrame.place(relx=.5, rely=.5,anchor="c")
        self.userLoginFrame.pack_forget()
        self.userDetailsPage()
        
    def userLoginPage(self):        
        login_label = Label(self.userLoginFrame, text="Login",background='light green', fg="#FFFFFF", font=("Arial", 30))
        username_label = Label(self.userLoginFrame, text="Username", background='light green', fg="#FFFFFF", font=("Arial", 16))
        username_entry = Entry(self.userLoginFrame, font=("Arial", 16),textvariable=self.user)
        login_button = Button(self.userLoginFrame, text="Login",background='white', font=("Arial", 16), command=self.change_to_userDetails)
        login_label.grid(row=0, column=0, columnspan=2, sticky="we", pady=40)
        username_label.grid(row=1, column=0,padx=5)
        username_entry.grid(row=1, column=1, pady=20, padx=5)
        login_button.grid(row=3, column=0, columnspan=2, pady=30)

    def userDetailsPage(self):        
        userName_label = Label(self.userDetailsFrame, text=self.user.get().upper(),background='light green', fg="#FFFFFF", font=("Arial", 30))
        userName_label.grid(row=0, column=0, columnspan=2, sticky="we", pady=40)
        reward_label = Label(self.userDetailsFrame, text="Rewards  :", background='light green', fg="#FFFFFF", font=("Arial", 16))
        reward_label.grid(row = 1,column=0,padx=5)
        rewards = self.db.getUserRewards(self.user.get().upper())
        if rewards==[]:
            rewardNone_label = Label(self.userDetailsFrame, text=" None", background='light green', fg="#FFFFFF", font=("Arial", 16))
            rewardNone_label.grid(row = 1,column=1,padx=5)
        else:
            for i,token in enumerate(rewards):
                cat = token[0][0]
                dis = token[0][1:-2]
                product = {"M":"Monitor","C":"Cable","X":"CPU","D":"Driver","K":"Keyboard","S":"Speaker","W":"Webcam","N":"Mouse"}
                strr = str(i) + ". " + str(token) + "  -  " + str(dis) + "% Off on : " + product[cat]
                rewardi_label = Label(self.userDetailsFrame, text=strr, background='light green', fg="#FFFFFF", font=("Arial", 16))
                rewardi_label.grid(row = 1,column=1+i,padx=5)

        


        submit_button = Button(self.userDetailsFrame, text="Submit",background='white', font=("Arial", 16), command=self.change_to_userLogin)
        submit_button.grid(row=3, column=0, columnspan=2, pady=30)
        logout_button = Button(self.userDetailsFrame, text="Logout",background='white', font=("Arial", 16), command=self.change_to_userLogin)
        logout_button.grid(row=3, column=0, columnspan=2, pady=30)


i = get_Input()
        
