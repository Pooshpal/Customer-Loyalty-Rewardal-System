import mysql.connector as mysq

class _database:
    def __init__(self) -> None:
        self.mydb = mysq.connect(
        host="localhost",
        user="root",
        password="password",
        database="mydatabase"
        )
        self.mycursor = self.mydb.cursor()

    def getUserRewards(self,username):
        self.mycursor.execute("SELECT reward FROM rewards WHERE userName = '%s'" % username)
        rewards = self.mycursor.fetchall()
        if rewards == []:return None
        else : return rewards

    def updateCustomer(self,total,username,reward_used,datetime):
        self.mycursor.execute("INSERT INTO customers (date, userName, totalBill, reward) VALUES (%s,%s,%s,%s)",(datetime,username,total,reward_used))
        self.mydb.commit()
        return self.mycursor.lastrowid

    def updateRewards_Add(self,datetime, username, reward, category, status):
        self.mycursor.execute("INSERT INTO rewards (date, userName, reward, category, status) VALUES (%s,%s,%s,%s,%s)",(datetime,username,reward,1,"ACTIVE"))
        self.mydb.commit()
        return self.mycursor.lastrowid

    def updateRewards_Update(self,reward):
        self.mycursor.execute("UPDATE rewards SET status = 'INACTIVE' WHERE reward = '%s'" % reward)
        self.mydb.commit()
        return self.mycursor.rowcount     

    def updateProducts(self,datetime, username, unitMonitor:int, unitCPU:int, unitDrivers:int, unitCable:int, unitKeyboard:int, unitSpeakers:int, unitWebcam:int, unitMouse:int):
        self.mycursor.execute("INSERT INTO products (date, userName, unitMonitor, unitCPU, unitDrivers, unitCable, unitKeyboard, unitSpeakers, unitWebcam, unitMouse) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(datetime,username,unitMonitor,unitCPU,unitDrivers,unitCable,unitKeyboard,unitSpeakers,unitWebcam,unitMouse))
        self.mydb.commit()
        return self.mycursor.lastrowid
        

