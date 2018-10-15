import datetime
import pprint
import pymongo


class Purchase:
    def __init__(self):
        my_client = pymongo.MongoClient("mongodb://localhost:27017")
        my_db = my_client.get_database("mydatabase")
        my_col = my_db["purchase_list"]
        self.purchase_list = my_col

    def add_new_position(self, my_dict):
        self.purchase_list.insert_one(my_dict)

    def delete_position(self, name):
        my_query = {"name": name}
        self.purchase_list.delete_one(my_query)

    def set_quantity(self, name, quantity):
        my_query = {"name": name}
        new_values = {"$set": {"quantity": quantity}}
        self.purchase_list.update_one(my_query, new_values)

    def set_purchase_date(self, name, date):
        my_query = {"name": name}
        new_values = {"$set": {"purchase_date": date}}
        self.purchase_list.update_one(my_query, new_values)

    def set_status(self, name, status):
        my_query = {"name": name}
        new_values = {"$set": {"status": status}}
        self.purchase_list.update_one(my_query, new_values)

    def get_all_positions(self):
        purchase_list = self.purchase_list.find({}, {"_id": 0, "name": 1, "quantity": 1, "unit_of_measurement": 1,
                                                     "purchase_date": 1, "status": 1})
        return purchase_list


if __name__ == '__main__':
    n = datetime.datetime.now().strftime("%Y/%m/%d")
    my_dict = {
        "name": "Spice",
        "quantity": 10,
        "unit_of_measurement": "grams",
        "purchase_date": n,
        "status": 0  # 0 - "To buy", 1 - "Bought"
    }
    purchase_list = Purchase().get_all_positions()
    for x in purchase_list:
        pprint.pprint(x)
        print('\n')
