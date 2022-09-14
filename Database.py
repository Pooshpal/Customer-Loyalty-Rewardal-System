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

