from flask import Blueprint, request, jsonify
from models import db, Product, Order
from flask_jwt_extended import jwt_required
from decorators import role_required

product_bp = Blueprint('product', __name__)
order_bp = Blueprint('order', __name__)

@product_bp.route('/products', methods=['GET'])
@jwt_required()
def get_products():
    products = Product.query.all()
    return jsonify([{"id": p.id, "name": p.name, "price": p.price} for p in products]), 200

@product_bp.route('/products', methods=['POST'])
@jwt_required()
@role_required('admin')
def add_product():
    data = request.get_json()
    product = Product(name=data['name'], description=data['description'], price=data['price'], quantity_in_stock=data['quantity_in_stock'])
    
    db.session.add(product)
    db.session.commit()
    return jsonify({"message": "Product added"}), 201

@product_bp.route('/products/<int:id>', methods=['DELETE'])
@jwt_required()
@role_required('admin')
def delete_product(id):
    product = Product.query.get(id)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product deleted"}), 200

@order_bp.route('/orders', methods=['POST'])
@jwt_required()
@role_required('customer')
def place_order():
    data = request.get_json()
    order = Order(product_id=data['product_id'], user_id=get_jwt_identity()['id'], quantity_ordered=data['quantity_ordered'])
    
    db.session.add(order)
    db.session.commit()
    return jsonify({"message": "Order placed"}), 201

@order_bp.route('/orders/<int:id>', methods=['DELETE'])
@jwt_required()
@role_required('admin')
def delete_order(id):
    order = Order.query.get(id)
    if not order:
        return jsonify({"error": "Order not found"}), 404

    db.session.delete(order)
    db.session.commit()
    return jsonify({"message": "Order deleted"}), 200
