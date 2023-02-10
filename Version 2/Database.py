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

    #get product details
    def getProductUnits(self,name):
        self.mycursor.execute("SELECT unitsSold,UnitsSold_Reward FROM products where productName = %s;",(name,))
        productInfo = self.mycursor.fetchall()
        return productInfo[0]
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

        visits = len(myresult)  # type: ignore
        if myresult != []:  userStatus = "LOYAL"
        else             :  userStatus = "NEW"

        self.mycursor.execute("SELECT * from logs where userName = %s AND rewardClaimed = 'True';",(userName,))
        myresult = self.mycursor.fetchall()
        claimed = len(myresult)  # type: ignore

        return userStatus,visits,claimed

    #get distinct usernames
    def getUserName(self):
        self.mycursor.execute("SELECT DISTINCT(userName) from logs;")
        myresult = self.mycursor.fetchall()
        users = list(a[0] for a in myresult)
        return users

    #get new and repeating customer details

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

    #get reward stats
    def getRewardStat(self):

        self.mycursor.execute("SELECT * from rewards;")
        total = self.mycursor.fetchall()
        total = len(total)

        self.mycursor.execute("SELECT rewardToken from rewards where status = 'CLAIMED';")
        claimed = self.mycursor.fetchall()
        claimed = len(claimed)

        self.mycursor.execute("SELECT rewardToken FROM rewards GROUP BY rewardToken ORDER BY COUNT(rewardToken) DESC LIMIT 1;")
        best = self.mycursor.fetchall()
        
        return total,claimed,best


        



class database_admin():

    def __init__(self) -> None:
        self.connection = _database()
    
    def __del__(self):
        del self.connection

    # ============================================================================================

    def userDashboard(self):
        data = {}
        users = self.connection.getUserName()
        for user in users:
            status,visits,claim = self.connection.getPast(userName=user)
            rewards = self.connection.getRewards(userName=user)
            data[user]={"Status":status,"Rewards":len(rewards),"Claimed":claim}
        return data

    def productDashboard(self):
        data = {}
        product_info = self.connection.getProductInfo()
        for (name,_) in product_info:
            unitsSold,Units_rewarded = self.connection.getProductUnits(name=name)
            boost = Units_rewarded*100/unitsSold
            data[name] = {"Units Sold":unitsSold,"Units Rewarded":Units_rewarded,"Boost":boost}
        return data

    def report(self):
        data = {}
        users = self.connection.getUserName()
        new = 0
        repeating = 0
        loyal = 0
        for user in users:
            status,visits,claim = self.connection.getPast(userName=user)
            if visits == 1:new = new + 1
            elif claim == 0:repeating = repeating + 1
            else: loyal = loyal + 1
        
        total,claim,best = self.connection.getRewardStat()

        data["New Users"]           =   new
        data["Repeating Users"]     =   repeating
        data["Loyal Users"]         =   loyal
        data["Rewardal Benefit"]    =   round(loyal*100/(new+loyal+repeating),2)
        data["Rewards Allocated"]   =   total
        data["Rewards Claimed"]     =   round(claim,2)
        data["Most Claimed Reward"] =   best[0][0]

        return data

