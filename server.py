from flask import Flask, request, jsonify, render_template, flash
from sql_connection import get_sql_connection
import json
import products_dao
import orders_dao

app = Flask(__name__)
app.secret_key = 'officus'
connection = get_sql_connection()

@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    response = orders_dao.get_all_orders(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getProducts', methods=['GET'])
def get_products():
    products = products_dao.get_all_products(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertOrder', methods=['POST'])
def insert_order():
    request_payload = json.loads(request.form['data'])
    if len(request_payload['order_details'][0]['product_id']) > 0:
        order_id = orders_dao.insert_order(connection, request_payload)
        response = jsonify({
            'order_id': order_id
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    else:
        print("error")

if __name__ == "__main__":
    print("Starting Python Flask Server For Grocery Store Management System")
    app.run(port=5000)
