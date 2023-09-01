from flask import Flask, request
app = Flask(__name__)


stores = [{
    "name" : "Big bazar",
    "items" : [{
        "name" : "chair",
        "price" : 23
    },
    {
        "name" : "pen", "price" : 10
    }]
}
]

print(stores)

@app.get("/store") #http://127.0.0.1:5000/store
def get_store():
    return {"stores" : stores}

@app.get("/product") #http://127.0.0.1:5000/product
def get_items():
    temp = []
    for i in stores:
        temp.extend(i["items"])
    return {"items" : temp}

@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name":request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return {"message":"Store not found"}, 404

@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"name" : request_data["name"], "items" :[]}
    stores.append(new_store)
    return new_store, 201

@app.get("/store/<string:name>/item")
def get_item(name):
    for store in stores:
        if store["name"] == name:
            return {"items" : store["items"]}, 201
    return {"message":"Store not found"}, 404