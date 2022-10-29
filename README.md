# Customer-Loyalty-Rewardal-System
A Database based system to be attached to an E-Commerce website to help reward loyal customers.


## Workflow

#### 1. User LogIn :
    - Enter Username and press submit.
    - Convert username to all lowercase.
    - If username is empty, reload page with error.
    - If SUCCESS : move this user to product page.

#### 2. Product Purchase:
    - Display : UserName, Rewards Available , Products to purchase and option to claim reward on that product, Logout & Purchase Option
    - SHow all products from database and options to buy multiple.
    - If no reward for a product - display NONE.
    - If reward available for a product, Display the percentage off
    - If LOGOUT - refresh and move to User Login.
    - If PURCHASE - move to Bill

#### 3. Bill:
    - Display : Username, Products & quantity bought and price after any discounts,rewards allocated, Logout Button.
    - Set Reward(If any) to status:claimed in database.
    - Allocate and display new rewards for the purchase to this user.
    - IF Logout - refresh and move to USer Login.


## Database Operations:

#### Databases : 
    - Log        [ dateTime(DateTime) , userName(String), rewardClaimed(Boolean), billTotal(Int) ]
    - Rewards    [ dateTime_allocated(DateTime), dateTime_claimed(DateTime), userName(String), rewardToken(UNIQUE String), category(Int), status(String)]
    - Products   [ productName(UNIQUE String), productPrice(Int), UnitsSold(Int), UnitsSold_Reward(Int)]

#### Operations On :
    - Log
        - For every purchase, INSERT information.
        - Use it to find repeating customers and find How many came back to claim the rewards ie. effectiveness of rewards
        - Find ratio of new customers to loyal customers.
    - Rewards
        - For every allocation, INSERT reward token and set status to UnClaimed.
        - For repeating every user Login, query all rewards of that user.
        - After a reward is claimed, UPDATE staus of reward to: Claimed
        - Statistics of all types and categorie of rewards allcoated and how many claimed of each category. Find effectiveness.
        - Find out statistics of fastest claimed / (Most Appealing) rewards.
        - Find out increase in product sales by checking reward claim dates.
    - Products
        - Query all products and prices to make product page.
        - UPDATE page on units sold.
        - Query page to find least trending product.
        - Find which products are trending depending on units sold ( without reward )


# Reward ALlocation Strategy & ASSUMPTIONS

#### Allocation Algorithm:
    - decide Category of reward based on bill amount. Category = [1,2,3,4,5]
    - find least selling product to reward (Category*10) % discount on that product.


#### ASSUMPTIONS:
    - Username is unique. no 2 users can have same username
    - A user may Claim only 1 reward per Bill.
    - Category 1 - Bill > 250
    - Category 2 - Bill > 500
    - Category 3 - Bill > 750
    - Category 4 - Bill > 1000
    - Category 5 - Bill > 1250
    


# Final Report : 

    - Customer 
        - Username
        - New or Ratio of rewards claimed to allocated
    - Products
        - Total Sale of products (with and without rewards)
        - Products sale increase/boost from rewards. Boost = sold_withReward / (TotalSold - sold_withReward)
    - Dashboard / Report
        - number of new customers
        - number of repeating customers
        - rewardal system benefit - number of repating customers who have claimed rewards.
        - ratio of claimed rewards to allocated rewards
        - Most appealing reward.
        - Statistics of category and number of rewards allocated in that category.


# Front End :

    - Rewardal System Portal for the company: 
        - Mobile Application in FLutter
        - Communicates through http packages.

    - Portal for users to take input:
        - basic tkinter setup to take input
        - directly running from python on a seperate thread.