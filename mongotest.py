import pymongo

client = pymongo.MongoClient("mongodb+srv://ats:ats11@cluster0.tupsxnu.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d= {
    'name':'att',
    'email': 'att@gmail.com',
    'surname':'shfgt'
}
db1= client['mongodb1']

coll= db1['test1']
coll.insert_one(d )