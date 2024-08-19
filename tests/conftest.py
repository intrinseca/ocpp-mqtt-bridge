from datetime import datetime
from unittest.mock import patch

import pytest


def fixed_now(tz=None):
    return datetime(2024, 3, 2, 12, 0, tzinfo=tz)


@pytest.fixture
def patch_datetime_now():
    with patch("datetime.datetime") as mock_datetime:
        mock_datetime.now.side_effect = fixed_now
        mock_datetime.combine.side_effect = datetime.combine
        yield mock_datetime
