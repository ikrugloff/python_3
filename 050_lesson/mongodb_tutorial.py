import pymongo
import datetime
import time
import pprint
"""
To create a database in MongoDB, start by creating a MongoClient object, then specify a connection URL with the correct 
ip address and the name of the database you want to create. MongoDB will create the database if it does not exist, 
and make a connection to it.
"""
my_client = pymongo.MongoClient("mongodb://localhost:27017")
my_db = my_client["mydatabase"]  # my_db = my_client.get_database("mydatabase")
"""
In MongoDB, a database is not created until it gets content!
MongoDB waits until you have created a collection (table), with at least one document (record) before it actually 
creates the database (and collection).
"""
# #  To check if a database exist by listing all databases in you system:
# print(my_client.list_database_names())
# # To check a specific database by name:
# dblist = my_client.list_database_names()
# if "purchase_list" in dblist:
#     print("The database exists.")
"""
In MongoDB, a collection is not created until it gets content!
MongoDB waits until you have inserted a document before it actually creates the collection.
"""
my_col = my_db["purchase_list"]  # collection = table
# # To check if a collection exist in a database by listing all collections:
# print(my_db.list_collection_names())
# # To check a specific collection by name:
# collist = my_db.list_collection_names()
# if "purchase_list" in collist:
#     print("The collection exists.")
"""
To insert a record, or document as it is called in MongoDB, into a collection, we use the insert_one() method.
The first parameter of the insert_one() method is a dictionary containing the name(s) and value(s) of each field in the 
document you want to insert.
"""
# d = datetime.datetime.strptime("2018/10/13 23:24", "%Y/%m/%d %H:%M")
# my_dict = {
#     "name": "Chicken breast",
#     "description": "It's a good source of protein and are low in fat and low in sodium.",
#     "quantity": 1,
#     "unit_of_measurement": "kilogram",
#     "purchase_date": d
# }
# x = my_col.insert_one(my_dict)
# print(x.inserted_id)
######
# d = datetime.datetime.strptime("2018/10/14 00:41", "%Y/%m/%d %H:%M")
# my_dict = {
#     "name": "Potatoes",
#     "description": "It's a starchy, tuberous crop from the perennial nightshade Solanum tuberosum.",
#     "quantity": 1,
#     "unit_of_measurement": "kilogram",
#     "purchase_date": d
# }
# y = my_col.insert_one(my_dict)
# print(y.inserted_id)
######
# d = datetime.datetime.strptime("2018/10/14", "%Y/%m/%d")
# my_list = [
#     {"name": "Chicken eggs", "quantity": 20, "unit_of_measurement": "pieces", "purchase_date": d},
#     {"name": "Mushrooms", "quantity": 500, "unit_of_measurement": "grams", "purchase_date": d},
#     {"name": "Cucumbers", "quantity": 1, "unit_of_measurement": "kilogram", "purchase_date": d},
#     {"name": "Tomatoes", "quantity": 1, "unit_of_measurement": "kilogram", "purchase_date": d},
#     {"name": "Vegetable oil", "quantity": 1, "unit_of_measurement": "liter", "purchase_date": d},
#     {"name": "Spice", "quantity": 10, "unit_of_measurement": "grams", "purchase_date": d}
# ]
# z = my_col.insert_many(my_list)
# print(z.inserted_ids)
"""
Insert Multiple Documents, with Specified IDs
If you do not want MongoDB to assign unique ids for you document, you can specify the _id field when you insert the 
document(s). Remember that the values has to be unique. Two documents cannot have the same _id.
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mylist = [
  { "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 5, "name": "Michael", "address": "Valley 345"},
  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
  { "_id": 9, "name": "Susan", "address": "One way 98"},
  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 12, "name": "William", "address": "Central st 954"},
  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]

x = mycol.insert_many(mylist)

#print list of the _id values of the inserted documents:
print(x.inserted_ids)
"""
"""
Find One
To select data from a collection in MongoDB, we can use the find_one() method.
The find_one() method returns the first occurrence in the selection.
"""
# d = datetime.datetime(2018, 10, 14).strftime("%Y/%m/%d")
# print(d)
# n = datetime.datetime.now().strftime("%Y/%m/%d")
# print(n)
# x = my_col.find_one()
# pprint.pprint(x)
######
# n = datetime.datetime.now().strftime("%Y/%m/%d")
# my_dict = {
#     "name": "Banana",
#     "description": "It's an edible fruit.",
#     "quantity": 1,
#     "unit_of_measurement": "kilogram",
#     "purchase_date": n
# }
# y = my_col.insert_one(my_dict)
# print(y.inserted_id)
"""
Find All
To select data from a table in MongoDB, we can also use the find() method.
The find() method returns all occurrences in the selection. The first parameter of the find() method is a query object. 
In this example we use an empty query object, which selects all documents in the collection.
"""
# for x in my_col.find():
#     pprint.pprint(x)
#     print('\n')
"""
Return Only Some Fields
The second parameter of the find() method is an object describing which fields to include in the result.
This parameter is optional, and if omitted, all fields will be included in the result.
"""
# for x in my_col.find({},{ "_id": 0, "name": 1, "purchase_date": 1}):  # 0 - exclude, 1 - include
#   pprint.pprint(x)
  # print('\n')

# for x in my_col.find({}, { "_id": 0, "name": 1, "quantity": 1, "unit_of_measurement": 1, "purchase_date": 1}):
#   pprint.pprint(x)
"""
Sort the Result
Use the sort() method to sort the result in ascending or descending order.
The sort() method takes one parameter for "fieldname" and one parameter for "direction" (ascending is the default 
direction).
"""
# my_doc = my_col.find({}, {"_id": 0, "name": 1}).sort("name", -1)  # 1 - ascending, -1 - descending
# for x in my_doc:
#   pprint.pprint(x)
"""
Delete Document
To delete one document, we use the delete_one() method.
The first parameter of the delete_one() method is a query object defining which document to delete.
Note: If the query finds more than one document, only the first occurrence is deleted.
"""
# my_doc = my_col.find({}, {"_id": 0, "name": 1}).sort("name", -1)  # 1 - ascending, -1 - descending
# for x in my_doc:
#   pprint.pprint(x)

# #Delete the document with the name "Spice":
# my_query = { "name": "Spice" }
# my_col.delete_one(my_query)

# my_doc = my_col.find({}, {"_id": 0, "name": 1}).sort("name", -1)  # 1 - ascending, -1 - descending
# for x in my_doc:
#   pprint.pprint(x)

# # Add the document with the name "Spice":
# n = datetime.datetime.now().strftime("%Y/%m/%d")
# my_dict = {
#     "name": "Spice",
#     "quantity": 10,
#     "unit_of_measurement": "grams",
#     "purchase_date": n
# }
# x = my_col.insert_one(my_dict)
#
# my_doc = my_col.find({}, {"_id": 0, "name": 1, "purchase_date": 1}).sort("name", -1)  # 1 - ascending, -1 - descending
# for x in my_doc:
#   pprint.pprint(x)
"""
Update Collection
You can update a record, or document as it is called in MongoDB, by using the update_one() method.
The first parameter of the update_one() method is a query object defining which document to update.
Note: If the query finds more than one record, only the first occurrence is updated.
The second parameter is an object defining the new values of the document.
"""
# n = datetime.datetime.now().strftime("%Y/%m/%d")
# my_query = {"name": "Vegetable oil"}
# new_values = {"$set": {"purchase_date": n}}
#
# my_col.update_one(my_query, new_values)
#
# # print "purchase_list" after the update:
# my_doc = my_col.find({}, {"_id": 0, "name": 1, "purchase_date": 1}).sort("name", -1)  # 1 - ascending, -1 - descending
# for x in my_doc:
#     pprint.pprint(x)
"""
Update Many
To update all documents that meets the criteria of the query, use the update_many() method.
"""
# n = datetime.datetime.now().strftime("%Y/%m/%d")
# my_query = {"name": {"$regex": "^[A-Z]"}}
# new_values = {"$set": {"purchase_date": n}}
#
# x = my_col.update_many(my_query, new_values)
#
# print(x.modified_count, "documents updated.")  # To count number of updated objects
# my_doc = my_col.find({}, {"_id": 0, "name": 1, "purchase_date": 1}).sort("name", -1)  # 1 - ascending, -1 - descending
# for x in my_doc:
#     pprint.pprint(x)
"""
Limit the Result
To limit the result in MongoDB, we use the limit() method.
The limit() method takes one parameter, a number defining how many documents to return.
"""
# my_doc = my_col.find({}, {"_id": 0, "name": 1, "purchase_date": 1}).sort("name", -1).limit(3)
# for x in my_doc:
#     pprint.pprint(x)
"""
Delete Collection
You can delete a table, or collection as it is called in MongoDB, by using the drop() method.
"""
# for x in my_col.find():
#     pprint.pprint(x)

# my_col.drop()

# n = datetime.datetime.now().strftime("%Y/%m/%d")
# my_list = [
#     {"name": "Chicken eggs", "quantity": 20, "unit_of_measurement": "pieces", "purchase_date": n, "status": 0},
#     {"name": "Mushrooms", "quantity": 500, "unit_of_measurement": "grams", "purchase_date": n, "status": 0},
#     {"name": "Cucumbers", "quantity": 1, "unit_of_measurement": "kilogram", "purchase_date": n, "status": 0},
#     {"name": "Tomatoes", "quantity": 1, "unit_of_measurement": "kilogram", "purchase_date": n, "status": 0},
#     {"name": "Vegetable oil", "quantity": 1, "unit_of_measurement": "liter", "purchase_date": n, "status": 0},
#     {"name": "Spice", "quantity": 10, "unit_of_measurement": "grams", "purchase_date": n, "status": 0}
# ]
# input_ = my_col.insert_many(my_list)
