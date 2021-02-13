import pytest

from app import create_app


def test_config(app):
    """Test create_app without passing test config."""
    assert create_app().testing


if __name__ == '__main__':
    # Calling pytest directly instead of the CLI
    pytest.main()
