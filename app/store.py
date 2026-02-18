"""In-memory store for the items API."""

from uuid import uuid4

_items: dict[str, dict] = {}


def list_items():
    return list(_items.values())


def get_item(item_id: str) -> dict | None:
    return _items.get(item_id)


def create_item(title: str) -> dict:
    item_id = str(uuid4())
    item = {"id": item_id, "title": title}
    _items[item_id] = item
    return item


def update_item(item_id: str, title: str) -> dict | None:
    if item_id not in _items:
        return None
    _items[item_id]["title"] = title
    return _items[item_id]


def delete_item(item_id: str) -> bool:
    if item_id not in _items:
        return False
    del _items[item_id]
    return True
