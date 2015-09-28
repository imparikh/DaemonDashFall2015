# This is written for PYTHON 3
# Don't forget to install requests package

import requests
import json
import ast
import array
import re
import time
import urllib2


class aParser:
	global customerId
	customerId = '55e94a6af8d8770528e60bbf'
	global apiKey
	apiKey = 'b5935eef2f80ce825ae84564a068b63d'
	global merchantId
	merchantId='55f472c035e65015006ceecb'
	global childAccId
	global purchaseArray
	purchaseArray=[]
	global dateArray
	dateArray= []
	global nameArray
	nameArray=[]
	global purchaseCount
	purchaseCount=0


	def setChild(self, childID):
		self.childAccId = childID

	def addBalanceToChildAcc(self, addition):
		url = 'http://api.reimaginebanking.com/accounts/{}/deposits?key={}'.format(self.childAccId,apiKey)
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

	def spending(self, name, subtraction, purchaseDate):
		url = 'http://api.reimaginebanking.com/accounts/{}/purchases?key={}'.format(self.childAccId,apiKey)
		urlGet = 'http://api.reimaginebanking.com/accounts/{}?key={}'.format(self.childAccId,apiKey)
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
			this.purchaseArray=this.purchaseArray
			print('Hello')
		else:
			purchaseArray.append(subtraction)
			dateArray.append(purchaseDate)
			nameArray.append(name)
			self.purchaseCount=purchaseCount+1
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
	
	def getBalance(self):
		urlGet = 'http://api.reimaginebanking.com/accounts/{}?key={}'.format(self.childAccId,apiKey)
		req = requests.get(
			urlGet,
			headers={'content-type':'application/json'},
		)
		content = req.content
		regx=re.search(r"balance\S:(\d+.?\d*),",content)
		return float(regx.group(1))






