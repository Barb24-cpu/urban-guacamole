from flask import Flask, send_file, jsonify, request
from orm import Inventory
from db import Database


app = Flask(__name__)

db = Database()
inventory = Inventory(db)


@app.route("/inventory", methods=["GET"])
def list_inventory():
    items = inventory.get_all_items()
    return jsonify(items)


@app.route("/inventory", methods=["POST"])
def add_inventory():
    data = request.get_json()

    new_item = inventory.add_item(
        name=data["name"],
        qty=data["qty"],
        buying_price=data["buying_price"],
        selling_price=data["selling_price"],
    )
    return (
        jsonify(
            {"message": "Item added successfully", "item": new_item}
        ),
        201,
    )


if __name__ == "__main__":
    app.run(debug=True)