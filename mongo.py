import os
import pymongo


if os.path.exists("env.py"):
    import env

MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myFirstDB"
COLLECTION = "celebrities"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("chuja dziala: %s") %e


conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]

coll.update_many({'nationality':'polish'},{'$set':{'hair_color': 'pink'}})

documents = coll.find({'nationality':'polish'})

for doc in documents:
    print(doc)