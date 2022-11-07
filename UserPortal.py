import enum
from tkinter import *
from turtle import color
import customtkinter
from matplotlib.dates import FR

# Starting a class to hold one session end to end. 
# Will store one username for one session.
# Will include - login page, product page & bill page.
class userPortal:
    # initialize a window for all frames.
    def __init__(self, win) -> None:
        self.win = win
        self.user = StringVar(value = "")
        self.win.configure(background="light blue")
        self.win.title("E Commerce Website")
        self.win.geometry("1800x800")
        self.win.resizable(0, 0)
        self.loginFrame  = Frame(background="light green",relief='sunken')
        self.loginFrame.place(relx=.5, rely=.5,anchor="c")
        self.loginPage()



    # Log In Page
    def loginPage(self, err = 0):        

        loginLabel     =   Label(self.loginFrame, text="Login",background='light green', fg="#FFFFFF", font=("Arial", 30))
        usernameLabel  =   Label(self.loginFrame, text="Username", background='light green', fg="#FFFFFF", font=("Arial", 16))
        usernameEntry  =   Entry(self.loginFrame, font=("Arial", 16),textvariable=self.user)
        errMsg         =   Label(self.loginFrame, text="Please Enter User Name !", background='light green', fg="red", font=("Arial", 13))
        loginButton    =   Button(self.loginFrame, text="Login",background='white', font=("Arial", 16), command=self.transitionToProduct)

        loginLabel.grid     (row=0, column=0, columnspan=2, sticky="we", pady=40)
        usernameLabel.grid  (row=1, column=0,padx=5)
        usernameEntry.grid  (row=1, column=1, pady=20, padx=5)
        if err:errMsg.grid  (row=2, column=1, pady=10, padx=5)
        loginButton.grid    (row=3, column=0, columnspan=2, pady=30)



    # Transition from Log In page to product Page.
    def transitionToProduct(self):

        # Fail
        if self.user.get() == "" or self.user == None:
            self.loginPage(err = 1)

        # Success
        else:
            for widget in self.loginFrame.winfo_children():
                widget.destroy()
            self.loginFrame.place_forget()
            self.productPage()



    def productPage(self, err = 0): 

        productPage = Frame(self.win, background="white")
        productPage.place(x=0,y=0,width=1800,height=800)

        # ==============================================================================
        # ================== HEADER ====================================================
        # ==============================================================================
        header = Frame(self.win, background="blue")
        header.place(x=10, y=10, height=80,width = 1780)

        welcomeLabel = Label(header, text="Welcome to DigiMart", fg="#FFFFFF",background='blue', font=("Arial", 30))
        welcomeLabel.place(y = 15,x = 700)

        # ==============================================================================
        # ================== SIDEBAR ===================================================
        # ==============================================================================
        
        # Fetch from database
        # Note: rewardsAvailable should : "rewardToken - productName @ 25%"
        userStatus,visitNumber, userRewardsClaimedCount, rewardsAvailable = ["NONE","NONE","NONE",["NONE"]]
        #rewardsAvailable = ["LP%20 - Laptop @ 20%","CP%25 - CPU @ 25%"]
        rewardsAvailable = []

        sidebar = Frame(self.win, bg='light blue')
        sidebar.place(x=30, y=120, width=330, height=650)
        
        usernameLabel = Label(sidebar, text="User Name: "+self.user.get().upper(),font=("Arial", 15),background="light blue",foreground="black")
        usernameLabel.place(x = 40, y= 120)

        statusLabel = Label(sidebar, text="Status : "+userStatus ,font=("Arial", 15),background="light blue",foreground="black" )
        statusLabel.place(x = 40, y= 160)

        visitLabel = Label(sidebar, text="No. Of Visits : "+visitNumber ,font=("Arial", 15),background="light blue",foreground="black" )
        visitLabel.place(x = 40, y= 200)
        
        rewardsClaimedLabel = Label(sidebar, text="Rewards Claimed : "+userRewardsClaimedCount ,font=("Arial", 15),background="light blue",foreground="black" )
        rewardsClaimedLabel.place(x = 40, y= 240)
        
        rewardsAvailableCountLabel = Label(sidebar, text="Rewards Available : "+str(len(rewardsAvailable)) ,font=("Arial", 15),background="light blue",foreground="black" )
        rewardsAvailableCountLabel.place(x = 40, y= 280)

        if len(rewardsAvailable) != 0:
            for count,r in enumerate(rewardsAvailable):
                Button(sidebar,text="          - "+r ,font=("Arial", 12),background="light pink",foreground="black" ).place(x = 40, y= 290+(count+1)*30,width=280,height=25)

        
        # =============================================================================
        # ======================== BODY ===============================================
        # =============================================================================

        # Fetch from database
        product_names , product_prices = [["None"],[0]]
        product_names  = ["Laptop","CPU","Monitor","Cables"]
        product_prices = [250,450,510,50]

        
        product_list = Frame(self.win,background="white")
        product_list.place(x = 380,y=120,width = 1400,height=600)
        
        product_list.grid_columnconfigure(0, weight=1)
        spinboxValues = []


        for count,(name,price) in enumerate(zip(product_names,product_prices)):
            Label(product_list,text=name ,font=("Arial", 15),background="light blue",foreground="white",width=25).grid(row=count, column=0,padx=5,pady=5)
            Label(product_list,text=price ,font=("Arial", 15),background="white",foreground="black",width=25,justify=CENTER ).grid(row=count, column=1,padx=5,pady=5)
            temp = Spinbox(product_list,from_=0,to_=10,width=10, font=("Helvetica",15)).grid(row=count,column=2,padx=5,pady=5)
            spinboxValues.append(temp)

        product_list.grid_columnconfigure(3, weight=1)

        # =============================================================================
        # ======================== FOOTER =============================================
        # =============================================================================  

        footer = Frame(self.win,background="light grey")
        footer.place(x = 380,y=700,width = 1400,height=70)

        logoutButton = customtkinter.CTkButton(master=self.win, text="Log Out",width=100,height=40)
        logoutButton.place(x = 940,y = 720)

        purchaseButton = customtkinter.CTkButton(master=self.win, text="Purchase",width=100,height=40)
        purchaseButton.place(x = 1140,y = 720)

    







customtkinter.set_default_color_theme("blue")
win = customtkinter.CTk()
test_run = userPortal(win)
win.mainloop()
