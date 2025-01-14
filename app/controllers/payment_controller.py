from app.models.payment import Payment
from app import db
from flask import jsonify, request
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.exceptions import BadRequest

# Utility function for input validation
def validate_input(data, required_keys):
    for key in required_keys:
        if key not in data or not data[key]:
            return False, f"{key} is required!"
    return True, ""

# Utility function to sanitize input
def sanitize_input(data):
    sanitized_data = {}
    for key, value in data.items():
        sanitized_data[key] = str(value).strip()  # Strip any extra spaces or characters
    return sanitized_data

# Create payment
def create_payment():
    try:
        data = request.get_json()
        data = sanitize_input(data)  # Sanitize input data

        required_keys = ["total_price"]
        is_valid, message = validate_input(data, required_keys)

        if not is_valid:
            raise BadRequest(message)

        total_price = data["total_price"]
        payment_method = data.get("payment_method", None)
        payment_status = data.get("payment_status", None)
        payment_date = data.get("payment_date", None)

        new_payment = Payment(
            total_price=total_price,
            payment_method=payment_method,
            payment_status=payment_status,
            payment_date=payment_date
        )
        db.session.add(new_payment)
        db.session.commit()

        return jsonify({"message": "Payment created successfully!"}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"message": f"Database Error: {str(e)}"}), 500
    except BadRequest as e:
        return jsonify({"message": str(e)}), 400
    except Exception as e:
        return jsonify({"message": f"Unexpected Error: {str(e)}"}), 500

# Get All payments
def get_all_payments():
    try:
        payments = Payment.query.all()
        return jsonify([payment.as_dict() for payment in payments]), 200
    except SQLAlchemyError as e:
        return jsonify({"message": f"Database Error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"message": f"Unexpected Error: {str(e)}"}), 500

# Get payment by ID
def get_payment_by_id(payment_id):
    try:
        payment = Payment.query.get(payment_id)
        if payment:
            return jsonify(payment.as_dict()), 200
        return jsonify({"message": "Payment not found!"}), 404
    except SQLAlchemyError as e:
        return jsonify({"message": f"Database Error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"message": f"Unexpected Error: {str(e)}"}), 500

# Update payment
def update_payment(payment_id):
    try:
        data = request.get_json()
        data = sanitize_input(data)  # Sanitize input data

        payment = Payment.query.get(payment_id)
        if payment:
            payment.total_price = data.get('total_price', payment.total_price)
            payment.payment_method = data.get('payment_method', payment.payment_method)
            payment.payment_status = data.get('payment_status', payment.payment_status)
            payment.payment_date = data.get('payment_date', payment.payment_date)

            db.session.commit()
            return jsonify({"message": "Payment updated successfully!"}), 200
        return jsonify({"message": "Payment not found!"}), 404
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"message": f"Database Error: {str(e)}"}), 500
    except BadRequest as e:
        return jsonify({"message": str(e)}), 400
    except Exception as e:
        return jsonify({"message": f"Unexpected Error: {str(e)}"}), 500

# Delete payment
def delete_payment(payment_id):
    try:
        payment = Payment.query.get(payment_id)
        if payment:
            db.session.delete(payment)
            db.session.commit()
            return jsonify({"message": "Payment deleted successfully!"}), 200
        return jsonify({"message": "Payment not found!"}), 404
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"message": f"Database Error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"message": f"Unexpected Error: {str(e)}"}), 500
