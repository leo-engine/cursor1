"""REST API routes."""

from flask import Blueprint, request, jsonify

from app.store import (
    list_items,
    get_item,
    create_item,
    update_item,
    delete_item,
)

api_bp = Blueprint("api", __name__, url_prefix="/api")


@api_bp.route("/items", methods=["GET"])
def items_list():
    """List all items."""
    return jsonify(list_items())


@api_bp.route("/items", methods=["POST"])
def items_create():
    """Create an item. Body: {"title": "..."}."""
    data = request.get_json() or {}
    title = data.get("title")
    if not title or not isinstance(title, str):
        return jsonify({"error": "title is required (string)"}), 400
    item = create_item(title.strip())
    return jsonify(item), 201


@api_bp.route("/items/<item_id>", methods=["GET"])
def items_get(item_id):
    """Get one item by id."""
    item = get_item(item_id)
    if item is None:
        return jsonify({"error": "not found"}), 404
    return jsonify(item)


@api_bp.route("/items/<item_id>", methods=["PUT"])
def items_update(item_id):
    """Update an item. Body: {"title": "..."}."""
    item = get_item(item_id)
    if item is None:
        return jsonify({"error": "not found"}), 404
    data = request.get_json() or {}
    title = data.get("title")
    if not title or not isinstance(title, str):
        return jsonify({"error": "title is required (string)"}), 400
    updated = update_item(item_id, title.strip())
    return jsonify(updated)


@api_bp.route("/items/<item_id>", methods=["DELETE"])
def items_delete(item_id):
    """Delete an item."""
    if not delete_item(item_id):
        return jsonify({"error": "not found"}), 404
    return "", 204
