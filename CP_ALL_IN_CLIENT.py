import pymongo

client = pymongo.MongoClient('mongodb+srv://fiapuser:<password>@<user>.ezuf3fx.mongodb.net/test')
db = client["<client>"]
collection = db["<colection>"]
get = collection.find_one()
print("OS DIRETÓRIOS ENCONTRADOS FORAM: ", get)
