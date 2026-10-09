"""Spike script to evaluate primary F1 data source (OpenF1).

Runs live probes to discover endpoints, fields, response latency, and rate limit behaviors.
"""

import json
import time
from typing import Any

import httpx


class APIProbe:
    """Encapsulates probing an external REST API endpoint."""

    def __init__(self, name: str, base_url: str, timeout: float = 10.0):
        self._name = name
        self._base_url = base_url.rstrip("/")
        self._timeout = timeout

    @property
    def name(self) -> str:
        return self._name

    @property
    def base_url(self) -> str:
        return self._base_url

    def fetch(self, endpoint: str, params: dict[str, Any] | None = None) -> tuple[int, float, Any, dict]:
        """Performs GET request, returning status_code, elapsed_seconds, parsed_json, headers."""
        url = f"{self._base_url}/{endpoint.lstrip('/')}"
        start = time.perf_counter()
        with httpx.Client(timeout=self._timeout) as client:
            response = client.get(url, params=params)
        elapsed = time.perf_counter() - start

        try:
            data = response.json()
        except (json.JSONDecodeError, ValueError):
            data = response.text

        return response.status_code, elapsed, data, dict(response.headers)


def probe_openf1() -> dict[str, Any]:
    print("\n--- Probing OpenF1 (https://api.openf1.org/v1) ---")
    probe = APIProbe("OpenF1", "https://api.openf1.org/v1")
    results = {}

    # 1. Probe Sessions (Bahrain 2024 Race)
    status, elapsed, data, headers = probe.fetch("/sessions", {"year": 2024, "country_name": "Bahrain", "session_name": "Race"})
    print(f"Sessions Endpoint: HTTP {status} in {elapsed:.3f}s | Records: {len(data) if isinstance(data, list) else 'N/A'}")
    if isinstance(data, list) and data:
        session_sample = data[0]
        session_key = session_sample.get("session_key")
        print(f"  Session Key: {session_key}, Circuit: {session_sample.get('circuit_short_name')}")
        results["session_sample"] = session_sample
    else:
        session_key = 9472 # fallback 2024 Bahrain Race key if needed

    # 2. Probe Laps
    status, elapsed, data, headers = probe.fetch("/laps", {"session_key": session_key, "driver_number": 1})
    print(f"Laps Endpoint (Driver 1): HTTP {status} in {elapsed:.3f}s | Laps: {len(data) if isinstance(data, list) else 'N/A'}")
    if isinstance(data, list) and data:
        results["lap_sample"] = data[0]
        print(f"  Sample lap fields ({len(data[0].keys())} fields): {list(data[0].keys())}")

    # 3. Probe Stints
    status, elapsed, data, headers = probe.fetch("/stints", {"session_key": session_key, "driver_number": 1})
    print(f"Stints Endpoint (Driver 1): HTTP {status} in {elapsed:.3f}s | Stints: {len(data) if isinstance(data, list) else 'N/A'}")
    if isinstance(data, list) and data:
        results["stint_sample"] = data[0]
        print(f"  Sample stint fields: {list(data[0].keys())}")

    # 4. Probe Pit Stops
    status, elapsed, data, headers = probe.fetch("/pit", {"session_key": session_key})
    print(f"Pit Endpoint: HTTP {status} in {elapsed:.3f}s | Pit Stops: {len(data) if isinstance(data, list) else 'N/A'}")
    if isinstance(data, list) and data:
        results["pit_sample"] = data[0]
        print(f"  Sample pit fields: {list(data[0].keys())}")

    results["headers"] = {k: v for k, v in headers.items() if "ratelimit" in k.lower() or "cache" in k.lower()}
    return results


if __name__ == "__main__":
    openf1_data = probe_openf1()

    output_path = "spikes/probe_results.json"
    with open(output_path, "w") as f:
        json.dump({"openf1": openf1_data}, f, indent=2)
    print(f"\nSaved raw probe summary to {output_path}")

