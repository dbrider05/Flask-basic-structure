## HTTP Put and Delete methods
## working with APIs -> JSON

from flask import Flask, jsonify, request

app = Flask(__name__)

# initial data in my to do list web app
items = [
    {'id':1,'name':'item1','description':'This is item 1'}, 
    {'id':2,'name':'item2','description':'This is item 2'}
]

@app.route('/')
def home():
    return "This is a sample TO DO List app"

# Get: retrieve all the items in the to do list
@app.route('/items',methods=['GET']) # you can use GET or get
def get_items():
    return jsonify(items) #Because Flask needs to return a proper HTTP response, and browsers or clients (like Postman, curl, or JavaScript fetch) expect data in a format they can understand — most commonly JSON.

# Get: retrieve a specific item in the to do list
@app.route('/items/<int:item_id>',methods=['Get'])
def get_item(item_id):
    item = next((item for item in items if item['id']==item_id),None)
    if item is None:
        return jsonify({'error':'Item not found'})
    return jsonify(item)

# Post: add a new item to the to do list - API waiting for JSON data to be sent 
@app.route('/items',methods=['POST'])
def add_item():
    if not request.json or 'name' not in request.json:
        return jsonify({'error':'Item not found'})
    new_item = {
        'id': items[-1]['id'] + 1,
        'name': request.json['name'],
        'description': request.json['description']
    }
    items.append(new_item)
    return jsonify(new_item)

# Put: update an existing item in the to do list
@app.route('/items/<int:item_id>',methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id']==item_id),None)
    if item is None:
        return jsonify({'error':'Item not found'})
    item['name'] = request.json.get('name',item['name'])
    item['description'] = request.json.get('description',item['description'])
    return jsonify(item)

# delete an item in the to do list
@app.route('/items/<int:item_id>',methods=['DELETE'])
def delete_item(item_id):
    item = next((item for item in items if item['id']==item_id),None)
    if item is None:
        return jsonify({'error':'Item not found'})
    items.remove(item)
    return jsonify({'result':'Item deleted'})


if __name__ == '__main__':
    app.run(debug=True)
