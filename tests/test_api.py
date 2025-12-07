from fastapi.testclient import TestClient
import pytest

from api.routes import app

client = TestClient(app)


def test_health():
    """Test health endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_query_endpoint():
    """Test query endpoint returns expected structure."""
    response = client.post(
        "/query",
        json={"query": "test query"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "answer" in data
    assert "citations" in data
    assert "request_id" in data
    assert "latency_ms" in data


def test_query_with_request_id():
    """Test query endpoint respects X-Request-ID header."""
    test_id = "test-request-123"
    response = client.post(
        "/query",
        json={"query": "test query"},
        headers={"X-Request-ID": test_id}
    )
    assert response.status_code == 200
    assert response.json()["request_id"] == test_id


def test_index_endpoint():
    """Test index rebuild endpoint."""
    response = client.post("/index")
    assert response.status_code == 200
    assert "status" in response.json()
    assert "request_id" in response.json()


# TODO: Add integration tests
# TODO: Add tests for retrieval modules
# TODO: Add tests for validators
