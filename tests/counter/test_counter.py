from src.counter import count_ocurrences
from unittest.mock import mock_open, patch

contain = "python, Python, PYTHON"


def test_counter():
    with patch("builtins.open", mock_open(read_data=contain)):
        assert count_ocurrences("src/jobs.csv", "python") == 3
