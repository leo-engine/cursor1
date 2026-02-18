"""Tests for the items REST API."""


def test_items_list_empty(client):
    """GET /api/items returns empty list initially."""
    r = client.get("/api/items")
    assert r.status_code == 200
    assert r.get_json() == []


def test_items_create(client):
    """POST /api/items creates an item and returns 201."""
    r = client.post(
        "/api/items",
        json={"title": "First item"},
        content_type="application/json",
    )
    assert r.status_code == 201
    data = r.get_json()
    assert data["title"] == "First item"
    assert "id" in data


def test_items_create_requires_title(client):
    """POST /api/items without title returns 400."""
    r = client.post("/api/items", json={}, content_type="application/json")
    assert r.status_code == 400


def test_items_crud_flow(client):
    """Create, get, update, list, delete."""
    # Create
    r = client.post(
        "/api/items",
        json={"title": "Test"},
        content_type="application/json",
    )
    assert r.status_code == 201
    item = r.get_json()
    item_id = item["id"]

    # Get one
    r = client.get(f"/api/items/{item_id}")
    assert r.status_code == 200
    assert r.get_json()["title"] == "Test"

    # Update
    r = client.put(
        f"/api/items/{item_id}",
        json={"title": "Updated"},
        content_type="application/json",
    )
    assert r.status_code == 200
    assert r.get_json()["title"] == "Updated"

    # List contains our item
    r = client.get("/api/items")
    assert r.status_code == 200
    items = r.get_json()
    our = next((i for i in items if i["id"] == item_id), None)
    assert our is not None and our["title"] == "Updated"

    # Delete
    r = client.delete(f"/api/items/{item_id}")
    assert r.status_code == 204

    # Get 404
    r = client.get(f"/api/items/{item_id}")
    assert r.status_code == 404


def test_items_get_404(client):
    """GET /api/items/<id> for unknown id returns 404."""
    r = client.get("/api/items/00000000-0000-0000-0000-000000000000")
    assert r.status_code == 404
