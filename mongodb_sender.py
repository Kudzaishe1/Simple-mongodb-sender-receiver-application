import pymongo  
from datetime import datetime

class Mongodb:
		def __init__(self):
				self.directory = "coord.txt"
				try:
					self.client = pymongo.MongoClient("mongodb+srv://kudzaishe:19990115@bde.uogpq.mongodb.net/BDE?retryWrites=true&w=majority")
					self.db = self.client["BDE_DATA"]
					self.collection = self.db["SENSOR_DATA"]
					print("CONNECTED AND READY TO GO")
				except:
					print("CONNECTION FAILED")

		def upload_file(self):
				try:
					with open(self.directory,"r") as file:
						date = datetime.now().date()
						DATA = {"location":"SOMERSET WEST","data":file.read(),"datetime":"{}_{}_{}".format(date.year,date.month,date.day)}
						file.close()
						self.collection.insert_one(DATA)
						print("Upload successful")
				except:
						print("Upload unsuccessful")

OBJECT = Mongodb()
OBJECT.upload_file()