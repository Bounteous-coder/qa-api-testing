from __future__ import annotations

import pytest

from src.api_client import ApiClient


BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.mark.parametrize(
    ("endpoint", "expected_status"),
    [
        ("/posts", 200),
        ("/posts/1", 200),
        ("/posts?userId=1", 200),
    ],
    ids=["TC-API-011", "TC-API-013", "TC-API-015"],
)
def test_posts_endpoints_expected_status(endpoint: str, expected_status: int) -> None:
    client = ApiClient(BASE_URL)
    response = client.get(endpoint)

    assert response.status_code == expected_status


def test_posts_list_returns_non_empty_array() -> None:
    client = ApiClient(BASE_URL)
    response = client.get("/posts")

    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, list)
    assert len(payload) >= 100


def test_single_post_id_matches_requested_record() -> None:
    client = ApiClient(BASE_URL)
    response = client.get("/posts/1")

    assert response.status_code == 200
    post = response.json()
    assert post["id"] == 1


def test_single_post_contains_required_fields() -> None:
    client = ApiClient(BASE_URL)
    response = client.get("/posts/1")

    assert response.status_code == 200
    post = response.json()
    for key in ["id", "userId", "title", "body"]:
        assert key in post


def test_posts_query_by_user_id_filters_results() -> None:
    client = ApiClient(BASE_URL)
    response = client.get("/posts?userId=1")

    assert response.status_code == 200
    posts = response.json()
    assert len(posts) > 0
    assert all(post["userId"] == 1 for post in posts)


@pytest.mark.parametrize("endpoint", ["/posts/0", "/posts/99999"], ids=["TC-API-018", "TC-API-019"])
def test_unknown_post_returns_404_or_empty_payload(endpoint: str) -> None:
    client = ApiClient(BASE_URL)
    response = client.get(endpoint)

    assert response.status_code in {404, 200}
    if response.status_code == 200:
        assert response.json() == {}


def test_create_post_returns_201_and_echoes_payload() -> None:
    client = ApiClient(BASE_URL)
    request_payload = {
        "title": "qa-check",
        "body": "validate create endpoint",
        "userId": 1,
    }

    response = client.post("/posts", request_payload)

    assert response.status_code == 201
    created = response.json()
    assert created["title"] == request_payload["title"]
    assert created["body"] == request_payload["body"]
    assert created["userId"] == request_payload["userId"]
    assert "id" in created


def test_create_post_assigns_numeric_id() -> None:
    client = ApiClient(BASE_URL)
    response = client.post(
        "/posts",
        {
            "title": "id-check",
            "body": "validate id type",
            "userId": 2,
        },
    )

    assert response.status_code == 201
    created = response.json()
    assert isinstance(created["id"], int)
