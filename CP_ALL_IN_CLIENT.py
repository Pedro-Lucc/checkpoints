import pymongo

client = pymongo.MongoClient('mongodb+srv://fiapuser:P3dr1nho@rm96036.ezuf3fx.mongodb.net/test')
db = client["cp4"]
collection = db["rm96036"]
get = collection.find_one()
print("OS DIRETÓRIOS ENCONTRADOS FORAM: ", get)
