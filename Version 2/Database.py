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
    def updateProducts(self, productCode, rewardClaimed = False):
        self.mycursor.execute("")
        self.mydb.commit()
        pass

    # ============================================================================================
    # ---------------------------------TABLE 2:LOG------------------------------------------------
    # ============================================================================================


    #Insert Log
    def insertLog(self, userName:str, bill:int ,rewardClaimed:str):
        self.mycursor.execute("INSERT into log (dateTime, userName, rewardClaimed, billTotal) VALUES (%s,%s,%s,%s);",(dt, userName, rewardClaimed, bill ))
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
        pass