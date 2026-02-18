"""Tests for web routes."""


def test_index_returns_200(client):
    """GET / returns 200."""
    r = client.get("/")
    assert r.status_code == 200


def test_index_contains_hello(client):
    """GET / contains Hello, World!."""
    r = client.get("/")
    assert b"Hello, World!" in r.data


def test_about_returns_200(client):
    """GET /about returns 200."""
    r = client.get("/about")
    assert r.status_code == 200


def test_about_contains_about(client):
    """GET /about contains About."""
    r = client.get("/about")
    assert b"About" in r.data


def test_health_returns_200(client):
    """GET /api/health returns 200."""
    r = client.get("/api/health")
    assert r.status_code == 200


def test_health_returns_json(client):
    """GET /api/health returns JSON with status ok."""
    r = client.get("/api/health")
    assert r.is_json
    assert r.get_json() == {"status": "ok"}
