from pymongo import MongoClient
client = MongoClient('mongodb+srv://lorenzopourpour:oaH5FYIScNlpfbPW@cluster0.7xubpdf.mongodb.net/')

db = client['sampledb']
emps_collection = db['emps']

emp = [{"empno": 9001,
       "empname": "Jeff Russell",
       "orders": [2608, 2617, 2620],
       "salary": 2800},
       {"empno": 9002,
        "empname": "Jane Boorman",
        "orders": [2610, 2615, 2619],
        "salary": 2700}]

#funzione per eliminare dati specifici
#db["emps"].delete_many({"empno": 9001})

result = emps_collection.insert_many(emp)
result.inserted_ids

emp_lista = list(emps_collection.find({"empno": 9001}))
print(emp_lista)