import pymongo

my_client = pymongo.MongoClient('mongodb://as-database:oHfA0NSURbklPgc5DVeLDnxDy1KaSHNJVrji28EMMT4FSrk4bandpHgx7qRYlgWRTx8g8wnr2rZ9ACDbpCZ30g==@as-database.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@as-database@')
mydb = my_client['book']
my_col = mydb['data']

print(mydb.list_collection_names())


book = {
    'id': '200',
    'title': 'SOME book 2',
    'author': 'Author 2'
}

my_col.insert_one(book)

for b in my_col.find():
    print(b)

print('it works')
