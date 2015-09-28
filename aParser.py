# This is just a parses that goes through all the data stored in the API.

import requests
import json
import ast
import re




class aParser:
	customerId = '55e94a6af8d8770528e60bbf'
	apiKey = 'b5935eef2f80ce825ae84564a068b63d'
	merchantId='55f472c035e65015006ceecb'
	childAccId = ""
	purchaseArray=[]
	dateArray= []
	nameArray=[]

	purchaseCount=0

#Sets the account of the ID of the child concerned 
	def setChild(self, childID):
		self.childAccId = childID

#This adds a certain balance to the child's account
	def addBalanceToChildAcc(self, addition):
		url = 'http://api.reimaginebanking.com/accounts/{}/deposits?key={}'.format(self.childAccId,self.apiKey)
		payload = {
    		"medium": "balance",
 	 		"transaction_date": "01012000",
  			"status": "completed",
  			"amount": float(addition),
  			"description": "deposit"
		}
		req = requests.post(
			url, 
			data=json.dumps(payload),
			headers={'content-type':'application/json'},
		)
		results_json_dump=json.dumps(ast.literal_eval(req.text))
		results_json=json.loads(results_json_dump)

#This spends a certain amount of money from the account
	def spending(self, name, subtraction, purchaseDate):
		url = 'http://api.reimaginebanking.com/accounts/{}/purchases?key={}'.format(self.childAccId,self.apiKey)
		urlGet = 'http://api.reimaginebanking.com/accounts/{}?key={}'.format(self.childAccId,self.apiKey)
		req = requests.get(
			urlGet,
			headers={'content-type':'application/json'},
		)
		content = req.content
		regx=re.search(r"balance\S:(\d+.?\d*),",content)
		currentBalance = float(regx.group(1))
		if (currentBalance<=float(subtraction)):
			#Cannot go through with purchase
			#Send email to parents
			self.purchaseArray=self.purchaseArray
			print('Hello')
		else:
			self.purchaseArray.append(subtraction)
			self.dateArray.append(purchaseDate)
			self.nameArray.append(name)
			self.purchaseCount=self.purchaseCount+1
			payload = {
				"merchant_id": "55f472c035e65015006ceecb",
				"medium": "balance",
				"purchase_date": "01012000",
				"amount": float(subtraction),
				"status": "completed",
				"description": "test"
			}
			req = requests.post(
				url, 
				data=json.dumps(payload),
				headers={'content-type':'application/json'},
			)
			results_json_dump=json.dumps(ast.literal_eval(req.text))
			results_json=json.loads(results_json_dump)

#this returns the balance of the account in question
	def getBalance(self):
		urlGet = 'http://api.reimaginebanking.com/accounts/{}?key={}'.format(self.childAccId,self.apiKey)
		req = requests.get(
			urlGet,
			headers={'content-type':'application/json'},
		)
		content = req.content
		regx=re.search(r"balance\S:(\d+.?\d*),",content)
		return float(regx.group(1))
	
	#This returns the day of the month the purchase was made
	def getDate(self):
		return self.dateArray

#This returns all the array of all the prices
	def getPurchases(self):
		return self.purchaseArray
	
##This returns the array of the names of all items bought
	def getNames(self):
		return self.nameArray


