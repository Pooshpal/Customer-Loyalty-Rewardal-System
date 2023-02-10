from Database import _database

class helper:

    def __init__(self,userName) -> None:
        self.userName = userName
        self.db = _database()
        pass
    
#===============================================================================================

    #Returns User Status, Number of previous Visits and Number of claimed rewards
    def getUserPast(self):
        return self.db.getPast(self.userName)
        
#===============================================================================================

    #Returns a List of all available rewards - Token and parsed into English
    def getUserRewards(self):
        rewardsToken_ = self.db.getRewards(userName= self.userName)
        rewardsToken = list(a[0] for a in rewardsToken_)
        rewardsAvailable = []
        for r in rewardsToken:
            temp = r + " - " + self.getProductName(r[:2]) + " @ " + r[3:] + " %"
            rewardsAvailable.append(temp)
        return rewardsToken,rewardsAvailable

#===============================================================================================
    
    #Returns a List of all product names and product prices
    def getProductInfo(self):
        productNames = []
        productPrices = []
        productInf = self.db.getProductInfo()
        for (name,price) in productInf:
            productNames.append(name)
            productPrices.append(price)
        return productNames, productPrices

#===============================================================================================

    #Return reward Allocated Token
    def allocateReward(self,bill):
        category = 1
        if bill < 250: category = 1
        elif bill < 500: category = 2
        elif bill < 750: category = 3
        elif bill < 1000: category = 4
        else : category = 5
        productCode = self.db.productNeedsHelp()
        rewardAllocated = productCode + "%" + str(category*10)
        return rewardAllocated, category

#===============================================================================================

    #Log a transaction, return bool
    def logIt(self,bill,reward:bool):
        success = self.db.insertLog(userName= self.userName, bill = bill, rewardClaimed = str(reward))
        return success

#===============================================================================================

    #Update reward claimed status in reward
    def rewardClaimed(self,token):
        sucess = self.db.updateReward(userName=self.userName,token=token)
        return sucess

#===============================================================================================

    #Update product info
    def updateProduct(self,purcahsedProducts:dict,rewardClaimed):
        sucess = True
        for (name,qty) in purcahsedProducts.items():
            if rewardClaimed!="NONE" and  name == self.getProductName(rewardClaimed[:2]):
                success = self.db.updateProducts(qty=qty, productName=name,rewardClaimed=qty)
            else:
                success = self.db.updateProducts(qty=qty, productName=name)
        return sucess

#===============================================================================================

    #Return product Name given Code
    def getProductName(self,code):
        productName = self.db.getProductName(code=code)
        return productName

#===============================================================================================

    #Insert allocated reward in rewards
    def insertAllocatedReward(self,token,category):
        success = self.db.insertReward(userName=self.userName,rewardAllocated=token,category=category)
        return success

#===============================================================================================

    def __del__(self):
        del self.db