from tkinter import *
from Database import _database


import datetime
dt = datetime.datetime.now()

class get_Input:
    def __init__(self) -> None:
        #connect to database
        self.db = _database()
        # create a GUI User window
        self.win = Tk()
        self.user = StringVar(value = "")
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
        self.userDetailsFrame.place_forget()
        self.user = StringVar(value = "")
        self.userLoginPage(err = 0)

    def change_to_userDetails(self,err=0):
        for widget in self.userLoginFrame.winfo_children():
            widget.destroy()
        if self.user.get().upper() == "" or self.user == None:self.userLoginPage(err = 1)
        else:
            self.userDetailsFrame.place(relx=.5, rely=.5,anchor="c")
            self.userLoginFrame.place_forget()
            self.userDetailsPage(err)

    def target_product(self):
        pass

    def allocate_rewards(self,total):
        pass
        

    def getTotal(self):
        self.reward_availed = self.reward_token.get()
        print("REWARD:",self.reward_availed,len(self.reward_availed))
        if self.reward_availed=="":self.reward_availed="NaN"
        rewards=[]
        if self.rewards !=None:
            for r in self.rewards:
               rewards.append(r[0]) 
        print("All rewards:",rewards,self.reward_availed in rewards)
        if rewards!=None and self.reward_availed not in rewards and self.reward_availed!="NaN":
            self.change_to_userDetails(err=2)
        else:
            price = {"M":200,"C":30,"X":250,"D":50,"K":25,"S":42,"W":37,"N":12}
            total = 0
            for prod,val in self.prod_units.items():
                if int(val.get()) > 0 and val.get()!=None:
                    total=total+(price[prod]*int(val.get()))
                    if self.reward_availed!="NaN"  and self.reward_availed[0] == prod:
                        dis = int(self.reward_availed[1:-2])/100
                        total =(price[prod]*(1-dis)*int(val.get()))
            print("TOTAL",total)
            if total == 0 : self.change_to_userDetails(err=1)
            else : 
                print("1 record inserted, ID:",self.db.updateCustomer(total=total,reward_used=self.reward_availed,username=self.user.get().upper(),datetime=dt))
                print("Rewards made INACTIVE: ",self.db.updateRewards_Update(reward=self.reward_availed))

                # Allocate Reward
                # Append rewards table
                self.change_to_userLogin()

            

    def userLoginPage(self, err =0):        
        login_label = Label(self.userLoginFrame, text="Login",background='light green', fg="#FFFFFF", font=("Arial", 30))
        username_label = Label(self.userLoginFrame, text="Username", background='light green', fg="#FFFFFF", font=("Arial", 16))
        username_entry = Entry(self.userLoginFrame, font=("Arial", 16),textvariable=self.user)
        err_msg = Label(self.userLoginFrame, text="Please Enter User Name !", background='light green', fg="red", font=("Arial", 13))
        login_button = Button(self.userLoginFrame, text="Login",background='white', font=("Arial", 16), command=self.change_to_userDetails)
        login_label.grid(row=0, column=0, columnspan=2, sticky="we", pady=40)
        username_label.grid(row=1, column=0,padx=5)
        username_entry.grid(row=1, column=1, pady=20, padx=5)
        if err:err_msg.grid(row=2, column=1, pady=10, padx=5)
        login_button.grid(row=3, column=0, columnspan=2, pady=30)

    def userDetailsPage(self, err = 0):   
        userName_label = Label(self.userDetailsFrame, text=self.user.get().upper(),background='light green', fg="#FFFFFF", font=("Arial", 30))
        userName_label.grid(row=0, column=0, columnspan=2, sticky="we", pady=40)
        reward_label = Label(self.userDetailsFrame, text="Rewards  :", background='light green', fg="#FFFFFF", font=("Arial", 20))
        reward_label.grid(row = 1,column=0,padx=5)
        self.rewards = self.db.getUserRewards(self.user.get().upper())
        self.prod_units = {"M":StringVar(value="0"),"C":StringVar(value="0"),"X":StringVar(value="0"),"D":StringVar(value="0"),"K":StringVar(value="0"),"S":StringVar(value="0"),"W":StringVar(value="0"),"N":StringVar(value="0")}
        product = {"M":"Monitor","C":"Cable","X":"CPU","D":"Driver","K":"Keyboard","S":"Speaker","W":"Webcam","N":"Mouse"}
        self.reward_token = StringVar(value="")
        r = 1
        if self.rewards==[] or self.rewards==None:
            rewardNone_label = Label(self.userDetailsFrame, text=" None", background='light green', fg="#FFFFFF", font=("Arial", 16))
            rewardNone_label.grid(row = r,column=1,padx=5)
        else:
            for i,token in enumerate(self.rewards):
                cat = token[0][0]
                dis = token[0][1:-2]
                strr = str(token[0]) + "  -  " + str(dis) + "% Off on : " + product[cat]
                rewardi_label = Label(self.userDetailsFrame, text=strr, background='light green', fg="#FFFFFF", font=("Arial", 16))
                rewardi_label.grid(row = r+i,column=1,padx=5)     
            r = r+i+1 
            avail_reward_label = Label(self.userDetailsFrame, text="Enter Reward Token : ", background='light green', fg="black", font=("Arial", 16))
            avail_reward = Entry(self.userDetailsFrame, font=("Arial", 16),textvariable=self.reward_token)
            avail_reward_label.grid(row = r,column=0,padx=10,pady=15)
            avail_reward.grid(row = r,column=1,padx=10,pady=15)
            r=r+1
        r=r+1

        # Place Product Menu
        available_prod_label = Label(self.userDetailsFrame, text="Available Products", background='red', fg="black", font=("Arial", 16))
        available_prod_label.grid(row = r,column=0,pady=10)
        r=r+1
        for prod,val in self.prod_units.items():
            prod_label = Label(self.userDetailsFrame, text=product[prod], background='light green', fg="black", font=("Arial", 16))
            prod_unit = Entry(self.userDetailsFrame, font=("Arial", 16),textvariable = val)
            prod_label.grid(row=r,column=0,padx=5,pady=5)
            prod_unit.grid(row=r,column=1,padx=10)
            r=r+1
        
        purchase_button = Button(self.userDetailsFrame, text="Purchase",background='white', font=("Arial", 16), command=self.getTotal)
        purchase_button.grid(row=r+1, column=0, pady=30)
        logout_button = Button(self.userDetailsFrame, text="Logout",background='white', font=("Arial", 16), command=self.change_to_userLogin)
        logout_button.grid(row=r+1, column=1, padx=5, pady=30)
        if err==1:
            err_msg = Label(self.userDetailsFrame, text="Please Purchase Something !", background='light green', fg="red", font=("Arial", 13))
            err_msg.grid(row=r+2, column=1, pady=10, padx=5)
        if err==2:
            err_msg = Label(self.userDetailsFrame, text="Wrong Reward Token !", background='light green', fg="red", font=("Arial", 13))
            err_msg.grid(row=r+2, column=1, pady=10, padx=5)



i = get_Input()
        
# allocate reward
# find least selling product
# finallu emter data in user log, product log, and reward list
# update reward list