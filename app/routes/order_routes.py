from flask import Blueprint
from app.middleware.auth_middleware import auth_required
from app.controllers.order_controller import (
    create_order,
    get_all_orders,
    get_order_by_id,
    update_order,
    delete_order
)

order_bp = Blueprint('order', __name__)

# Protected routes (auth required)
order_bp.route('/', methods=['POST'])(create_order)
order_bp.route('/', methods=['GET'])(get_all_orders)
order_bp.route('/<int:order_id>', methods=['GET'])(get_order_by_id)
order_bp.route('/<int:order_id>', methods=['PUT'])(update_order)
order_bp.route('/<int:order_id>', methods=['DELETE'])(delete_order)
