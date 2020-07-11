  import os

try:
	import pymongo
	import yaml
except:
	os.system("pip install PyYAML")
	os.system("pip install pymongo")
	import yaml
	import pymongo

class Mongodb:

		def __init__(self):
				try:
					self.client = pymongo.MongoClient("<API KEY>")
					self.db = self.client["DATABASE NAME"]
					self.collection = self.db["COLLECTION NAME"]
					print(self.client.test)
				except:
					print("CONNECTION FAILED")

		def save_file(self):
				try:
					data = [str(objects) for objects in self.collection.find({})]
					print(data[0])
					data = yaml.load(data[0])
					
					directory = r"{}_{}.txt".format(data["location"],data['datetime']) #QUERY EXAMPLE
					with open(directory,"w") as file:
						file.write(data["data"])
						os.system("hdfs dfs -put {} /SENSOR_DATA/".format(directory)) #HDFS EXAMPLE
						print("successful")
						self.collection.delete_many({})
				except:
						print("FAILED")
					

OBJECT = Mongodb()
OBJECT.save_file()