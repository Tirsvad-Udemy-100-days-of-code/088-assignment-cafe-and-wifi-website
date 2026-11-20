"""Tests of the constants module."""

from cafe_wifi import constants


def test_default_port_is_unprivileged() -> None:
    """The default port is above the privileged range."""
    assert constants.DEFAULT_PORT > 1024


def test_default_host_is_loopback() -> None:
    """The development server only listens on the loopback address."""
    assert constants.DEFAULT_HOST == "127.0.0.1"
