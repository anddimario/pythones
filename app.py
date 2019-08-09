from flask import Flask, jsonify, request
from api import movements
from api import movements_stats
from flask_expects_json import expects_json

app = Flask(__name__)

schema = {
    'type': 'object',
    'properties': {
        'orderId': {'type': 'string'},
        'sku': {'type': 'string'},
        'quantity': {'type': 'number'},
        'price': {'type': 'number'}
    },
    'required': ['orderId', 'sku', 'productName', 'quantity', 'price']
}


@app.route("/")
def hello():
    return "Hello, World!"

# MOVEMENTS
@app.route("/movements", methods=["POST"])
@expects_json(schema)
def add():
    request_json = request.get_json()
    movements.add(request_json)
    return jsonify({'success': 'true'})

@app.route("/movements/<id>")
def get(id):
    hit = movements.get(id)    
    return jsonify({'success': 'true', 'value': hit})

@app.route("/movements/orders/<id>")
def get_order(id):
    hits = movements.get_order(id)    
    return jsonify({'success': 'true', 'value': hits})

@app.route("/movements")
def get_all():
    hits = movements.get_all()
    return jsonify({'success': 'true', 'value': hits})

# MOVEMENTS STATS
@app.route("/stats/movements/total/price")
def total_price():
    results = movements_stats.total_price()
    return jsonify({'success': 'true', 'value': results})

@app.route("/stats/movements/total/quantity")
def total_quantity():
    results = movements_stats.total_quantity()
    return jsonify({'success': 'true', 'value': results})

@app.route("/stats/movements/total/orders/<id>")
def total_order(id):
    results = movements_stats.total_order(id)
    return jsonify({'success': 'true', 'value': results})

@app.route("/stats/movements/total/products/<id>")
def total_product(id):
    results = movements_stats.total_product(id, request.args)
    return jsonify({'success': 'true', 'value': results})

@app.route("/stats/movements/total/buyers/<id>")
def total_buyer(id):
    results = movements_stats.total_buyer(id, request.args)
    return jsonify({'success': 'true', 'value': results})

@app.route("/stats/movements/best/buyers")
def best_buyers():
    results = movements_stats.best_buyers()
    return jsonify({'success': 'true', 'value': results})

@app.route("/stats/movements/best/products")
def best_products():
    results = movements_stats.best_products()
    return jsonify({'success': 'true', 'value': results})

# error handling
@app.errorhandler(404)
def page_not_found(e):
    return jsonify(error=404, text=str(e)), 404

@app.errorhandler(500)
def page_error(e):
    return jsonify(error=500, text=str(e)), 500