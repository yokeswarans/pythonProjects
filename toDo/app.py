#put and delete-http verbs
#Working with API --Json

from flask import Flask,jsonify, request

app=Flask(__name__)

#Initialize data in my todo list

items=[
    {"id":1,"name":"Item1","description":"This is the item 1"},
    {"id":2,"name":"Item2","description":"This is the item 2"}
]

@app.route('/')
def home():
    return "Welcome to the sample todo list app"

#GET : Retrieve all the item

@app.route('/items',methods=['GET'])
def get_items():
    return jsonify(items)

#GET :Retrieve the specific item by id
@app.route('/items/<int:item_id>',methods=["GET"])
def get_item(item_id):
    item=next((item for item in items if item["id"]==item_id),None)
    if item is None:
        return jsonify({"error":"item not found"})
    return jsonify(item)

##POST :create a new task
@app.route('/items',methods=["POST"])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error":"Items not found"})
    new_items={
        "id":items[-1]["id"]+1 if items else 1,
        "name":request.json['name'],
        "description":request.json["description"]
    }
    items.append(new_items)
    return jsonify(new_items)

#PUT : Update an existing item
@app.route('/items/<int:item_id>',methods=['PUT'])
def update_item(item_id):
    item=next((item for item in items if item["id"]==item_id),None)
    if item is None:
        return jsonify({"error":"Item is not found"})
    item['name']=request.json.get('name',item['name'])
    item['description']=request.json.get('description',item['description'])
    return jsonify(item)

#DELETE: delete an item
@app.route('/items/<int:item_id>',methods=['DELETE'])
def delete_item(item_id):
    global items
    items=[item for item in items if item["id"]!=item_id]
    return jsonify({'result':"Item Deleted"})

hello world


if __name__=='__main__':
    app.run(debug=True)
