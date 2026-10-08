"""Initial smoke test to verify test harness and package import."""

import pitwall


def test_package_import():
    assert pitwall.__version__ == "0.1.0"
