import mysql.connector as mysq
import datetime
dt = datetime.datetime.now()

class _database:
    def __init__(self) -> None:
        self.mydb = mysq.connect(
        host="localhost",
        user="root",
        password="password",
        database="dataBucket"
        )
        self.mycursor = self.mydb.cursor()
    
    def __del__(self):
        self.mycursor.close()
        self.mydb.close()

    # ============================================================================================
    # ---------------------------------TABLE 1:RPODUCTS-------------------------------------------
    # ============================================================================================

    #Update Product Unit Sold and Units Sold - Rewarded
    def updateProducts(self, productName, qty, rewardClaimed = 0):
        self.mycursor.execute("UPDATE products set unitsSold = unitsSold + %s,UnitsSold_Reward = UnitsSold_Reward + %s WHERE productName = %s ;",(qty,rewardClaimed,productName))
        self.mydb.commit()
        return True

    #get product Name from code
    def getProductName(self,code):
        self.mycursor.execute("SELECT productName from products where productCode = %s;",(code,))
        myresult = self.mycursor.fetchall()
        return myresult[0][0]

    #get product Info
    def getProductInfo(self):
        self.mycursor.execute("SELECT productName,productPrice FROM products;")
        productInfo = self.mycursor.fetchall()
        return productInfo

    #get least sold product Name
    def productNeedsHelp(self):
        self.mycursor.execute("SELECT productCode FROM products WHERE unitsSold IN (SELECT MIN(unitsSold) FROM products);")
        productCodes = self.mycursor.fetchall()
        return productCodes[0][0]


    # ============================================================================================
    # ---------------------------------TABLE 2:LOG------------------------------------------------
    # ============================================================================================


    #Insert Log
    def insertLog(self, userName:str, bill:int ,rewardClaimed:str):
        self.mycursor.execute("INSERT into logs (dateTime, userName, rewardClaimed, billTotal) VALUES (%s,%s,%s,%s);",(dt, userName, rewardClaimed, bill ))
        self.mydb.commit()
        return True


    #Get past
    def getPast(self,userName):

        self.mycursor.execute("SELECT * from logs where userName = %s;",(userName,))
        myresult = self.mycursor.fetchall()

        visits = len(myresult)
        if myresult != []:  userStatus = "LOYAL"
        else             :  userStatus = "NEW"

        self.mycursor.execute("SELECT * from logs where userName = %s AND rewardClaimed = 'True';",(userName,))
        myresult = self.mycursor.fetchall()
        claimed = len(myresult)

        return userStatus,visits,claimed



    # ============================================================================================
    # ---------------------------------TABLE 3:REWARDS--------------------------------------------
    # ============================================================================================

    #Insert New Reward
    def insertReward(self,userName:str, rewardAllocated:str, category:int):
        self.mycursor.execute("INSERT into rewards (dateTime_allocated, dateTime_claimed, userName, rewardToken, category, status) VALUES (%s,%s,%s,%s,%s,%s);",(dt,None,userName, rewardAllocated, category,"ACTIVE"))
        self.mydb.commit()
        return True

    #Get Rewards of users
    def getRewards(self,userName:str):
        self.mycursor.execute("SELECT rewardToken from rewards where userName = %s;",(userName,))
        myresult = self.mycursor.fetchall()
        return myresult

    #Update status of reward
    def updateReward(self,userName,token):
        self.mycursor.execute("UPDATE rewards set status = 'CLAIMED',dateTime_claimed = %s WHERE userName = %s AND rewardToken = %s;",(dt,userName,token))
        self.mydb.commit()
        return True
