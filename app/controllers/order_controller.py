from app.models.order import Order
from app import db
from flask import jsonify, request
from sqlalchemy.exc import SQLAlchemyError

# Utility function for input validation
def validate_input(data, required_keys):
    for key in required_keys:
        if key not in data or not data[key]:
            return False, f"{key} is required!"
    return True, ""

# Create order
def create_order():
    try:
        data = request.get_json()
        required_keys = ["number_table", "number_of_people"]
        is_valid, message = validate_input(data, required_keys)

        if not is_valid:
            return jsonify({"message": message}), 400

        payment_id = data.get("payment_id", None)
        number_table = data["number_table"]
        number_of_people = data["number_of_people"]

        new_order = Order(
            payment_id=payment_id,
            number_table=number_table,
            number_of_people=number_of_people
        )
        db.session.add(new_order)
        db.session.commit()

        return jsonify({"message": "Order created successfully!"}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"message": f"Database Error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"message": f"Unexpected Error: {str(e)}"}), 500

# Get All orders
def get_all_orders():
    try:
        orders = Order.query.all()
        return jsonify([order.as_dict() for order in orders]), 200
    except SQLAlchemyError as e:
        return jsonify({"message": f"Database Error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"message": f"Unexpected Error: {str(e)}"}), 500

# Get order by ID
def get_order_by_id(order_id):
    try:
        order = Order.query.get(order_id)
        if order:
            return jsonify(order.as_dict()), 200
        return jsonify({"message": "Order not found!"}), 404
    except SQLAlchemyError as e:
        return jsonify({"message": f"Database Error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"message": f"Unexpected Error: {str(e)}"}), 500

# Update order
def update_order(order_id):
    try:
        data = request.get_json()
        order = Order.query.get(order_id)
        if order:
            order.payment_id = data.get('payment_id', order.payment_id)
            order.number_table = data.get('number_table', order.number_table)
            order.number_of_people = data.get('number_of_people', order.number_of_people)

            db.session.commit()
            return jsonify({"message": "Order updated successfully!"}), 200
        return jsonify({"message": "Order not found!"}), 404
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"message": f"Database Error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"message": f"Unexpected Error: {str(e)}"}), 500

# Delete order
def delete_order(order_id):
    try:
        order = Order.query.get(order_id)
        if order:
            db.session.delete(order)
            db.session.commit()
            return jsonify({"message": "Order deleted successfully!"}), 200
        return jsonify({"message": "Order not found!"}), 404
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"message": f"Database Error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"message": f"Unexpected Error: {str(e)}"}), 500
