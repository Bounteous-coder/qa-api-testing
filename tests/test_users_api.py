from __future__ import annotations

import time

import pytest

from src.api_client import ApiClient


BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.mark.parametrize(
    ("endpoint", "expected_status"),
    [
        ("/users", 200),
        ("/users/1", 200),
        ("/users/5", 200),
    ],
    ids=["TC-API-001", "TC-API-005", "TC-API-007"],
)
def test_users_endpoints_expected_status(endpoint: str, expected_status: int) -> None:
    client = ApiClient(BASE_URL)
    response = client.get(endpoint)

    assert response.status_code == expected_status


def test_users_list_is_non_empty_array() -> None:
    client = ApiClient(BASE_URL)
    response = client.get("/users")

    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, list)
    assert len(payload) > 0


def test_users_list_has_expected_count() -> None:
    client = ApiClient(BASE_URL)
    response = client.get("/users")

    assert response.status_code == 200
    payload = response.json()
    assert len(payload) == 10


def test_single_user_contains_required_fields() -> None:
    client = ApiClient(BASE_URL)
    response = client.get("/users/1")

    assert response.status_code == 200
    user = response.json()
    for key in ["id", "name", "email", "username", "address", "company"]:
        assert key in user


def test_user_id_matches_requested_record() -> None:
    client = ApiClient(BASE_URL)
    response = client.get("/users/1")

    assert response.status_code == 200
    user = response.json()
    assert user["id"] == 1


@pytest.mark.parametrize("endpoint", ["/users/0", "/users/99999"], ids=["TC-API-008", "TC-API-009"])
def test_unknown_user_returns_404_or_empty_payload(endpoint: str) -> None:
    client = ApiClient(BASE_URL)
    response = client.get(endpoint)

    # JSONPlaceholder may return {} with 404 depending on endpoint behavior.
    assert response.status_code in {404, 200}
    if response.status_code == 200:
        assert response.json() == {}


def test_users_endpoint_under_latency_threshold() -> None:
    client = ApiClient(BASE_URL)
    start = time.perf_counter()
    response = client.get("/users")
    elapsed_ms = (time.perf_counter() - start) * 1000

    assert response.status_code == 200
    assert elapsed_ms < 1200


@pytest.mark.parametrize("user_id", [2, 7], ids=["TC-API-006", "TC-API-010"])
def test_selected_users_have_valid_email(user_id: int) -> None:
    client = ApiClient(BASE_URL)
    response = client.get(f"/users/{user_id}")

    assert response.status_code == 200
    user = response.json()
    assert "@" in user["email"]
