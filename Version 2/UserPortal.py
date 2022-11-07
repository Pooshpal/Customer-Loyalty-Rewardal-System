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
        
        # Fetch from database
        # Note: rewardsAvailable should : "rewardToken - productName @ 25%"
        userStatus,visitNumber, userRewardsClaimedCount, self.rewardsAvailable = ["NONE","NONE","NONE",["NONE"]]
        self.rewardTokenAvailable = ["LP%20","CP%25"]
        self.rewardsAvailable = ["LP%20 - Laptop @ 20%","CP%25 - CPU @ 25%"]
        #rewardsAvailable = []

        self.sidebar = Frame(self.win, bg='light blue')
        self.sidebar.place(x=30, y=120, width=330, height=650)
        
        usernameLabel = Label(self.sidebar, text="User Name: "+self.user.get().upper(),font=("Arial", 15),background="light blue",foreground="black")
        usernameLabel.place(x = 40, y= 120)

        statusLabel = Label(self.sidebar, text="Status : "+userStatus ,font=("Arial", 15),background="light blue",foreground="black" )
        statusLabel.place(x = 40, y= 160)

        visitLabel = Label(self.sidebar, text="No. Of Visits : "+visitNumber ,font=("Arial", 15),background="light blue",foreground="black" )
        visitLabel.place(x = 40, y= 200)
        
        rewardsClaimedLabel = Label(self.sidebar, text="Rewards Claimed : "+userRewardsClaimedCount ,font=("Arial", 15),background="light blue",foreground="black" )
        rewardsClaimedLabel.place(x = 40, y= 240)
        
        rewardsAvailableCountLabel = Label(self.sidebar, text="Rewards Available : "+str(len(self.rewardsAvailable)) ,font=("Arial", 15),background="light blue",foreground="black" )
        rewardsAvailableCountLabel.place(x = 40, y= 280)

        self.rewardUsed = StringVar(value = "Enter Reward Token")
        if len(self.rewardsAvailable) != 0:
            Entry(self.sidebar, font=("Arial", 16), textvariable=self.rewardUsed).place(x = 40, y= 310,width=280,height=25)
            for count,r in enumerate(self.rewardsAvailable):
                Button(self.sidebar,text="          - "+r ,font=("Arial", 12),background="light pink",foreground="black" ).place(x = 40, y= 310+(count+1)*30,width=280,height=25)
        
        # =============================================================================
        # ======================== BODY ===============================================
        # =============================================================================

        # Fetch from database
        self.product_names , self.product_prices = [["None"],[0]]
        self.product_names  = ["Laptop","CPU","Monitor","Cables"]
        self.product_prices = [250,450,510,50]

        
        self.product_list = Frame(self.win,background="white")
        self.product_list.place(x = 380,y=120,width = 1400,height=600)
        
        self.product_list.grid_columnconfigure(0, weight=1)
        self.spinboxValues = {}


        for count,(name,price) in enumerate(zip(self.product_names,self.product_prices)):
            Label(self.product_list,text=name ,font=("Arial", 15),background="light blue",foreground="white",width=25).grid(row=count, column=0,padx=5,pady=5)
            Label(self.product_list,text=price ,font=("Arial", 15),background="white",foreground="black",width=25,justify=CENTER ).grid(row=count, column=1,padx=5,pady=5)
            temp = IntVar()
            Spinbox(self.product_list,from_=0,to_=10,width=10,textvariable=temp, font=("Helvetica",15)).grid(row=count,column=2,padx=5,pady=5)
            self.spinboxValues["item{0}".format(count)] = temp
        self.product_list.grid_columnconfigure(3, weight=1)

        # =============================================================================
        # ======================== FOOTER =============================================
        # =============================================================================  

        self.footer = Frame(self.win,background="light grey")
        self.footer.place(x = 380,y=700,width = 1400,height=70)

        self.logoutButton = customtkinter.CTkButton(master=self.win, text="Log Out",width=100,height=40)
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

        # Get product Name from Token Product code using sql.
        if rewardToken_flag and reward_applicable:
            token = self.rewardUsed.get().strip()
            code = token[:2]
            discount = int(token[3:])
            rewardProduct = "Laptop"

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


        print("Bill: ",bill)
        print("Reward Used:",self.rewardUsed.get())
        #print("Reward Code:",code)
        print("Is reward Token Valid:",rewardToken_flag)
        print("Is reward product purchased",reward_flag)
        print("Is bill 0:",bill==0)
        
        

               
 
        if not rewardToken_flag:
            self.helper_reset()
            self.productPage(err=2) 

        elif bill == 0 : 
            self.helper_reset()
            self.productPage(err=1) 

        elif not reward_flag:
            self.helper_reset()
            self.productPage(err=3) 

        else:
            self.helper_reset()
            self.checkoutPage()


# Final Page to see bill and checkout
    def checkoutPage(self):

        self.check = Frame(self.win,background="white")
        self.check.place(x = 600,y=100,width = 600,height=400)

        billHeading = Label()
        billHeading.grid()
         
        forUserDate = Label()
        forUserDate.grid()

        line = Label()
        line.grid()

        for count,pro,pr in enumerate(self.purchasedProducts):
            Label().grid()

        line.grid()

        rewardLabel = Label()
        rewardLabel.grid()

        rewarded = Label()
        rewarded.grid()

        

        
    
#Helper Functions
    def helper_reset(self):
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





customtkinter.set_default_color_theme("blue")
win = customtkinter.CTk()
test_run = userPortal(win)
win.mainloop()
