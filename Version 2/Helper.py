from Database import _database

class helper:

    def __init__(self,userName) -> None:
        self.user = userName
        pass
    

    #Returns User Status, Number of previous Visits and Number of claimed rewards
    def getUserPast(self):
        userStatus = "NEW"
        visits = 0
        claimed = 0
        return userStatus, visits, claimed
        

    #Returns a List of all available rewards - Token and parsed into English
    def getUserRewards(self): 
        rewardsToken = []
        rewardsAvailable = []
        return rewardsToken,rewardsAvailable

    
    #Returns a List of all product names and product prices
    def getProductInfo(self):
        productNames = []
        productPrices = []
        return productNames, productPrices


    #Return reward Allocated Token
    def allocateReward(self,bill):
        rewardAllocated = ""
        return rewardAllocated

    #Log a transaction, return bool
    def logIt(self,bill,reward:bool):
        success = True
        return success

    #Update reward claimed status
    def rewardClaimed(self,token):
        sucess = True
        return sucess

    #Update product info
    def updateProduct(self,purcahsedProducts:dict,rewardClaimed):
        if rewardClaimed == "None":
            pass
        sucess = True
        return sucess

    #Return product Name given Code
    def getProductName(self,code):
        productName = ""
        return productName
