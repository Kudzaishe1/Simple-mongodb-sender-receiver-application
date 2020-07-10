import pymongo  
import os

try:
	import yaml
except:
	os.system("pip install PyYAML")
	import yaml

class Mongodb:

		def __init__(self):
				try:
					self.client = pymongo.MongoClient("mongodb+srv://kudzaishe:19990115@bde.uogpq.mongodb.net/BDE?retryWrites=true&w=majority")
					self.db = self.client["BDE_DATA"]
					self.collection = self.db["SENSOR_DATA"]
					print(self.client.test)
				except:
					print("CONNECTION FAILED")

		def save_file(self):
				try:
					data = [str(objects) for objects in self.collection.find({})]
					print(data[0])
					data = yaml.load(data[0])
					
					directory = r"{}_{}.txt".format(data["location"],data['datetime'])
					with open(directory,"w") as file:
						file.write(data["data"])
						os.system("hdfs dfs -put {} /SENSOR_DATA/".format(directory))
						print("successful")
						self.collection.delete_many({})
				except:
						print("FAILED")
					

OBJECT = Mongodb()
OBJECT.save_file()