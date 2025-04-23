from db import get_db

collection = get_db()

def add_product(name, category, quantity, price):
    product = {
        "name": name,
        "category": category,
        "quantity": quantity,
        "price": price
    }
    return collection.insert_one(product)

def get_all_products_with_id():
    products = list(collection.find({}))
    for p in products:
        p['_id'] = str(p['_id'])
    return products

def delete_product(product_id):
    from bson.objectid import ObjectId
    return collection.delete_one({"_id": ObjectId(product_id)})

def update_product(product_id, updates):
    from bson.objectid import ObjectId
    return collection.update_one({"_id": ObjectId(product_id)}, {"$set": updates})
