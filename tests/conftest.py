from datetime import datetime, timezone
from unittest.mock import patch

import pytest


def fixed_now(tz=None):
    return datetime(2024, 1, 2, 12, 0, tzinfo=timezone.utc).astimezone(tz)


def fixed_now_summer(tz=None):
    return datetime(2024, 7, 2, 12, 0, tzinfo=timezone.utc).astimezone(tz)


def fixed_now_dst(tz=None):
    return datetime(2024, 3, 31, 12, 0, tzinfo=timezone.utc).astimezone(tz)


@pytest.fixture
def patch_datetime_now():
    with patch("datetime.datetime") as mock_datetime:
        mock_datetime.now.side_effect = fixed_now
        mock_datetime.combine.side_effect = datetime.combine
        yield mock_datetime


@pytest.fixture
def patch_datetime_now_summer():
    with patch("datetime.datetime") as mock_datetime:
        mock_datetime.now.side_effect = fixed_now_summer
        mock_datetime.combine.side_effect = datetime.combine
        yield mock_datetime


@pytest.fixture
def patch_datetime_now_dst():
    with patch("datetime.datetime") as mock_datetime:
        mock_datetime.now.side_effect = fixed_now_dst
        mock_datetime.combine.side_effect = datetime.combine
        yield mock_datetime
