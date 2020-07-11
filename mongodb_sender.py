import pymongo  
from datetime import datetime

class Mongodb:
		def __init__(self):
				self.directory = ""
				try:
					self.client = pymongo.MongoClient("<API KEY>")
					self.db = self.client["<YOUR DATABASE>"] 
					self.collection = self.db["<YOUR COLLECTION>"]
					print("CONNECTED AND READY TO GO")
				except:
					print("CONNECTION FAILED")

		def upload_file(self):
				try:
					with open(self.directory,"r") as file:
						date = datetime.now().date()
						DATA = {"location":"SOMERSET WEST","data":file.read(),"datetime":"{}_{}_{}".format(date.year,date.month,date.day)} #DEMO QUERY 
						file.close()
						self.collection.insert_one(DATA)
						print("Upload successful")
				except:
						print("Upload unsuccessful")

OBJECT = Mongodb()
OBJECT.upload_file()