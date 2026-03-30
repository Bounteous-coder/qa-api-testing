from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import requests


@dataclass
class ApiClient:
    base_url: str
    timeout: float = 5.0

    def get(self, path: str) -> requests.Response:
        return requests.get(f"{self.base_url}{path}", timeout=self.timeout)

    def post(self, path: str, payload: dict[str, Any]) -> requests.Response:
        return requests.post(f"{self.base_url}{path}", json=payload, timeout=self.timeout)
