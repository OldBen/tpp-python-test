from pymongo import MongoClient, errors

server = "localhost"
port = 27017
client = MongoClient(server, port)

try:
    db = client["tpp"]
    col = db["entries"]

    msg = "Please input your message: "
    entry = input(msg)
    length = len(entry)
    record = { "length" : length, "input" : entry}
    col.insert_one(record)
    entries = col.find().sort("length")
    for doc in entries:
        print("(" + str(doc["length"]) + ")\t" + doc["input"])
except errors.ConnectionFailure:
    err_msg = "Failed to connect to database"
    print (err_msg)
finally:
    client.close()