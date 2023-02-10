import enum
from tkinter import *
from turtle import color
import customtkinter
from matplotlib.dates import FR
import datetime
from Helper import helper


# Starting a class to hold one session end to end. 
# Will store one username for one session.
# Will include - login page, product page & bill page.


class userPortal:

    # initialize a window for all frames.
    def __init__(self, win) -> None:
        self.win = win
        self.win.configure(background="light blue")
        self.win.title("E Commerce Website")
        self.win.geometry("1800x800")
        self.win.resizable(0, 0)
        self.loginPage()



    # Log In Page
    def loginPage(self, err = 0):        

        self.loginFrame  = Frame(background="light green",relief='sunken')
        self.loginFrame.place(relx=.5, rely=.5,anchor="center")
        self.user = StringVar(value = "")

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
            print("Debug: User name EMPTY, reloading Login Page")
            self.loginPage(err = 1)

        # Success
        else:
            for widget in self.loginFrame.winfo_children():
                widget.destroy()
            self.loginFrame.place_forget()
            self.help = helper(self.user.get().lower().strip())
            print("Debug: Login : SUCCESS, Initializing Connection to helper.")
            print("Debug: User: ",self.user.get().upper()) 
            self.productPage()



    def productPage(self, err = 0): 

        self.productPageframe = Frame(self.win, background="white")
        self.productPageframe.place(x=0,y=0,width=1800,height=800)

        # ==============================================================================
        # ================== HEADER ====================================================
        # ==============================================================================
        self.header = Frame(self.win, background="blue")
        self.header.place(x=10, y=10, height=80,width = 1780)

        welcomeLabel = Label(self.header, text="Welcome to DigiMart", fg="#FFFFFF",background='blue', font=("Arial", 30))
        welcomeLabel.place(y = 15,x = 700)

        # ==============================================================================
        # ================== SIDEBAR ===================================================
        # ==============================================================================
        
        # Fetch past from database
        # Note: rewardsAvailable should : "rewardToken - productName @ 25%"
        userStatus, visitNumber, userRewardsClaimedCount = self.help.getUserPast()
        print("Debug: Fetching from database        : help.getUserPast()")
        print("Debug: User Status                   :",userStatus)
        print("Debug: User Visit Number             :",visitNumber)
        print("Debug: User Reward Claimed Count     :",userRewardsClaimedCount) 

        # Fetch reward details from Database
        # Note: self.rewardTokenAvailable = ["LP%20","CP%25"]
        # Note: self.rewardsAvailable = ["LP%20 - Laptop @ 20%","CP%25 - CPU @ 25%"]
        self.rewardTokenAvailable, self.rewardsAvailable  = self.help.getUserRewards()
        print("Debug: Fetching from database        : help.getUserRewards()")
        print("Debug: User Reward Tokens Available  :",self.rewardTokenAvailable)
        print("Debug: User Rewards Available        :",self.rewardsAvailable)


        self.sidebar = Frame(self.win, bg='light blue')
        self.sidebar.place(x=30, y=120, width=330, height=650)
        
        usernameLabel = Label(self.sidebar, text="User Name: "+self.user.get().upper(),font=("Arial", 15),background="light blue",foreground="black")
        usernameLabel.place(x = 40, y= 120)

        statusLabel = Label(self.sidebar, text="Status : "+userStatus ,font=("Arial", 15),background="light blue",foreground="black" )
        statusLabel.place(x = 40, y= 160)

        visitLabel = Label(self.sidebar, text="No. Of Visits : "+str(visitNumber) ,font=("Arial", 15),background="light blue",foreground="black" )
        visitLabel.place(x = 40, y= 200)
        
        rewardsClaimedLabel = Label(self.sidebar, text="Rewards Claimed : "+str(userRewardsClaimedCount) ,font=("Arial", 15),background="light blue",foreground="black" )
        rewardsClaimedLabel.place(x = 40, y= 240)
        
        rewardsAvailableCountLabel = Label(self.sidebar, text="Rewards Available : "+str(len(self.rewardsAvailable)) ,font=("Arial", 15),background="light blue",foreground="black" )
        rewardsAvailableCountLabel.place(x = 40, y= 280)

        self.rewardUsed = StringVar(value = "Enter Reward Token")
        if len(self.rewardsAvailable) != 0:
            Entry(self.sidebar, font=("Arial", 16), textvariable=self.rewardUsed).place(x = 40, y= 310,width=280,height=25)
            for count,r in enumerate(self.rewardsAvailable):
                Button(self.sidebar,text=r ,font=("Arial", 12),background="light pink",foreground="black" ).place(x = 40, y= 310+(count+1)*30,width=280,height=25)
        
        # =============================================================================
        # ======================== BODY ===============================================
        # =============================================================================

        # Fetch product info from database
        # Note: self.product_names  = ["Laptop","CPU","Monitor","Cables"]
        # NOte: self.product_prices = [250,450,510,50]
        self.product_names, self.product_prices = self.help.getProductInfo()
        print("Debug: Fetching from database        : help.getProductInfo()")
        print("Debug: Product Names                 :",self.product_names)
        print("Debug: Product Prices                :",self.product_prices)
        
        self.product_list = Frame(self.win,background="white")
        self.product_list.place(x = 380,y=120,width = 1400,height=600)
        
        self.product_list.grid_columnconfigure(0, weight=1)
        self.spinboxValues = {}

        for count,(name,price) in enumerate(zip(self.product_names,self.product_prices)):
            Label(self.product_list,text=name ,font=("Arial", 15),background="light blue",foreground="white",width=25).grid(row=count, column=0,padx=5,pady=5)
            Label(self.product_list,text=price ,font=("Arial", 15),background="white",foreground="black",width=25,justify=CENTER ).grid(row=count, column=1,padx=5,pady=5)
            temp = IntVar()
            Spinbox(self.product_list,from_=0,to=10,width=10,textvariable=temp, font=("Helvetica",15)).grid(row=count,column=2,padx=5,pady=5)
            self.spinboxValues["item{0}".format(count)] = temp
        self.product_list.grid_columnconfigure(3, weight=1)

        # =============================================================================
        # ======================== FOOTER =============================================
        # =============================================================================  

        self.footer = Frame(self.win,background="light grey")
        self.footer.place(x = 380,y=700,width = 1400,height=70)

        self.logoutButton = customtkinter.CTkButton(master=self.win, text="Log Out",width=100,height=40,command=self.logout)
        self.logoutButton.place(x = 940,y = 725)

        self.purchaseButton = customtkinter.CTkButton(master=self.win, text="Purchase",width=100,height=40,command=self.transitionToCheckout)
        self.purchaseButton.place(x = 1140,y = 725)

        if err == 0:        self.footer.place_forget()
        if err == 1:        Label(self.footer, text="Purchase Something !", background='light green', fg="red", font=("Arial", 13)).pack()
        if err == 2:        Label(self.footer, text="Reward Token INVALID !", background='light green', fg="red", font=("Arial", 13)).pack()
        if err == 3:        Label(self.footer, text="Reward Not Applicable !", background='light green', fg="red", font=("Arial", 13)).pack()


# Transition from Product page to Checkout Page.
    def transitionToCheckout(self):
        
        bill = 0
        reward_flag = True
        rewardToken_flag = True
        reward_applicable = True

        #Check if reward token is correct.
        if self.rewardUsed.get() not in self.rewardTokenAvailable:
            if self.rewardUsed.get() != "Enter Reward Token":
                rewardToken_flag = False
            else:
                reward_applicable = False
                
        print("Debug: Reward Used       :",self.rewardUsed.get())
        print("Debug: Reward Applicable :",reward_applicable)
        print("Debug: Reward Valid      :",rewardToken_flag)

        # Get product Name from Token Product from Database
        if rewardToken_flag and reward_applicable:
            token = self.rewardUsed.get().strip()
            code = token[:2]
            discount = int(token[3:])
            #rewardProduct = "Laptop"
            rewardProduct = self.help.getProductName(code)
            print("Debug: Fetching from database        : help.getProductName()")
            print("Debug: User Reward Token for Product :",rewardProduct)
            print("Debug: Token Discount on product     :",discount)

        self.purchasedProducts = {}
        for count,pr in enumerate(self.product_prices):
            val = self.spinboxValues["item{0}".format(count)].get() * pr
            if reward_applicable and self.product_names[count]==rewardProduct:
                if val == 0:
                    reward_flag = False
                elif rewardToken_flag and val!=0: 
                    val = (100-discount)/100*val
            if val != 0:
                self.purchasedProducts[self.product_names[count]] =  self.spinboxValues["item{0}".format(count)].get()
            bill = bill + val

        
        print("Debug: Purchased Products:",self.purchasedProducts)
        print("Debug: Bill              :",bill)

        if not rewardToken_flag:
            self.helper_reset()
            print("Debug: Reward Token Invalid")
            self.productPage(err=2) 

        elif bill == 0 : 
            self.helper_reset()
            print("Debug: Purchase Something")
            self.productPage(err=1) 

        elif not reward_flag:
            self.helper_reset()
            print("Debug: Reward Product Not Purchased")
            self.productPage(err=3) 

        else:
            self.helper_reset()
            if reward_applicable:
                self.rewardClaimed = token
            else:
                self.rewardClaimed = "NONE"
            print("Debug: Reward Claimed        :",self.rewardClaimed)
            print("Debug: Product Page Success, Initiating CHeckout")
            self.totalBill = bill
            self.checkoutPage()


# Final Page to see bill and checkout
    def checkoutPage(self):

        #Allocate reward and Feed to Database
        rewardAllocated, category = self.help.allocateReward(self.totalBill)
        success = self.help.insertAllocatedReward(rewardAllocated, category)
        print("Debug: Fetching from database        : help.allocateReward()")
        print("Debug: Reward Allocated to User      :",rewardAllocated)
        print("Debug: Reward Allocated Category     :",category)

        #Log This transaction into Database
        success = self.help.logIt(self.totalBill, self.rewardClaimed!="NONE")
        print("Debug: Fetching from database        : help.logIt()")
        print("Debug: Transaction Log               :",success)

        #Update products info in database
        success = self.help.updateProduct(self.purchasedProducts,self.rewardClaimed)
        print("Debug: Fetching from database        : help.updateProduct()")
        print("Debug: Update product                :",success)

        #Update reward claimed status in Database if used
        if self.rewardClaimed != "None":
            success = self.help.rewardClaimed(self.rewardClaimed)
            print("Debug: Fetching from database        : help.rewardClaimed()")
            print("Debug: Updating Reward Claimed       :",success)


        self.check = Frame(self.win,background = "white")
        self.check.place(x = 600,y=100,width = 600,height=400)

        Label(self.check,text="",background="white").grid(row=1)
        billHeading = Label(self.check, text = "BILL" ,font=("Arial", 30),background="light blue",foreground="black" )
        billHeading.grid(row=2,column=0)
        
        line1= Label(self.check, text = "-------------------------------------------------------------------------------------" ,font=("Arial", 15),background="white",foreground="black")
        line1.grid(row = 3,column=0)
        
        forUserDate = Label(self.check, text = str("\nUser :"+self.user.get().upper()+"               Date:"+str(datetime.date.today())) ,font=("Arial", 13),background="white",foreground="black")
        forUserDate.grid(row = 4,column=0)

        line2= Label(self.check, text = "-------------------------------------------------------------------------------------" ,font=("Arial", 10),background="white",foreground="black")
        line2.grid(row=5,column=0)

        for count,(pro,pr) in enumerate(self.purchasedProducts.items()):
            Label(self.check, text = str(str(count+1) + " - " + pro + "     - x" + str(pr)) ,background="white",font=("Arial", 15),foreground="black").grid(row = 6+count)

        line3= Label(self.check, text = "-------------------------------------------------------------------------------------" ,font=("Arial", 15),background="white",foreground="black")
        line3.grid(row=7+count)

        rewardLabel = Label(self.check, text = str("Reward Used : "+self.rewardClaimed) ,background="white",font=("Arial", 13),foreground="black")
        rewardLabel.grid(row = 8+count)

        rewarded = Label(self.check, text = str("You are Rewarded : "+rewardAllocated) ,background="white",font=("Arial", 13),foreground="black")
        rewarded.grid(row = 9+count)

        line4= Label(self.check, text = "-------------------------------------------------------------------------------------" ,font=("Arial", 15),background="white",foreground="black")
        line4.grid(row = 10+count)

        bill = Label(self.check, text = str("                                                      Total Bill : "+str(self.totalBill)) ,background="white",font=("Arial", 15),foreground="red")
        bill.grid(row = 11+count)


        self.FlogoutButton = customtkinter.CTkButton(master=self.win, text="Log Out",width=100,height=40,command=self.transitionToLogin)
        self.FlogoutButton.place(x = 850,y = 455)
        

    def transitionToLogin(self):
        for widget in self.check.winfo_children():
            widget.destroy()
        self.check.place_forget()
        self.FlogoutButton.destroy()
        print("Debug: Logout User           :",self.user.get().upper())
        del self.help
        self.loginPage()

    def logout(self):
        self.helper_reset()
        print("Debug: Logout User:",self.user.get().upper())
        del self.help
        self.loginPage()
    
#In-Class components Helper Functions
    def helper_reset(self):
        print("Debug: Resetting Product Page")
        for widget in self.productPageframe.winfo_children():
            widget.destroy()
        for widget in self.footer.winfo_children():
            widget.destroy()
        for widget in self.header.winfo_children():
            widget.destroy()
        for widget in self.product_list.winfo_children():
            widget.destroy()
        for widget in self.sidebar.winfo_children():
            widget.destroy()
        self.productPageframe.place_forget()
        self.product_list.place_forget()
        self.header.place_forget()
        self.footer.place_forget()
        self.sidebar.place_forget()
        self.logoutButton.destroy()
        self.purchaseButton.destroy()





# customtkinter.set_default_color_theme("blue")
# win = customtkinter.CTk()
# test_run = userPortal(win)
# win.mainloop()
