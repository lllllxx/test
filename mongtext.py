import pymongo

# client = pymongo.MongoClient(host='10.12.65.20', port=27017)
uri = "mongodb://user:password@example.com/default_db?authSource=admin"
client = pymongo.MongoClient(uri)
db = client.visitor
collection = db.address_detail_copy1
