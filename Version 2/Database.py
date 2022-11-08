import mysql.connector as mysq
import datetime
dt = datetime.datetime.now()

class _database:
    def __init__(self) -> None:
        self.mydb = mysq.connect(
        host="localhost",
        user="root",
        password="password",
        database="datBucket"
        )
        self.mycursor = self.mydb.cursor()

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
    def insertLog(self, userName:str, bill:int ,rewardClaimed:bool):
        self.mycursor.execute("INSERT into log (dateTime, userName, rewardClaimed, billTotal) VALUES (%s,%s,%s,%s);",(dt, userName, rewardClaimed, bill ))
        self.mydb.commit()
        pass

    #

    # ============================================================================================
    # ---------------------------------TABLE 3:REWARDS--------------------------------------------
    # ============================================================================================

    #Insert New Reward
    def insertReward(self,userName:str, rewardAllocated:str, category:int):
        self.mycursor.execute("INSERT into rewards (dateTime_allocated, dateTime_claimed, userName, rewardToken, category, status) VALUES (%s,%s,%s,%s,%s,%s);",(dt,None,userName, rewardAllocated, category,"ACTIVE"))
        self.mydb.commit()
        pass