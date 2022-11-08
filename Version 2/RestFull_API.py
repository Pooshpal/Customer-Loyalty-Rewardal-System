from flask import Flask, jsonify, request
from Database import database_admin

class api():

    def __init__(self) -> None:
        print("Debug: API BOOTING UP")
        self.app = Flask(__name__)
        self.letsPutItUp()
        self.app.run(debug=True, port=8080)
        

    def letsPutItUp(self):

        @self.app.route('/', methods = ['GET'])
        def test():
            return jsonify({'version':'2.0'})

#=======================================================================================================

        """
        userDashboard :
        dataPacket = 
        {
            "mihir": {
              "Claimed": 1,
              "Rewards": 2,
              "Status": "LOYAL"
            },
            "naman": {
              "Claimed": 0,
              "Rewards": 2,
              "Status": "LOYAL"
            },
            "pooshpal": {
              "Claimed": 4,
              "Rewards": 6,
              "Status": "LOYAL"
            },
            "tom": {
              "Claimed": 2,
              "Rewards": 4,
              "Status": "LOYAL"
            }
        }       
        
        """
        
        @self.app.route('/userDashboard', methods = ['GET'])
        def returnAlluser():
            temp = database_admin()
            dataPacket = temp.userDashboard()
            del temp
            return jsonify(dataPacket)

#=======================================================================================================
        """
        product Dashboard:
        datapacket = 
        {
          "CPU": {
            "Boost": 0.0,
            "Units Rewarded": 0,
            "Units Sold": 6
          },
          "Cables": {
            "Boost": 0.0,
            "Units Rewarded": 0,
            "Units Sold": 6
          },
          "GPU": {
            "Boost": 100.0,
            "Units Rewarded": 2,
            "Units Sold": 2
          },
          "Keyboard": {
            "Boost": 33.333333333333336,
            "Units Rewarded": 1,
            "Units Sold": 3
          },
          "Laptop": {
            "Boost": 16.666666666666668,
            "Units Rewarded": 1,
            "Units Sold": 6
          },
          "Monitor": {
            "Boost": 0.0,
            "Units Rewarded": 0,
            "Units Sold": 6
          },
          "Mouse": {
            "Boost": 0.0,
            "Units Rewarded": 0,
            "Units Sold": 2
          },
          "RAM": {
            "Boost": 0.0,
            "Units Rewarded": 0,
            "Units Sold": 1
          }
        }
        
        """

        @self.app.route('/productDashboard', methods = ['GET'])
        def returnAllproduct():
            temp = database_admin()
            dataPacket = temp.productDashboard()
            del temp
            return jsonify(dataPacket)

#=======================================================================================================

        """
        product Dashboard:
        datapacket = 

        """
        @self.app.route('/report', methods = ['GET'])
        def returnAllreport():
            temp = database_admin()
            dataPacket = temp.report()
            del temp
            return jsonify(dataPacket)

        
#test = api()