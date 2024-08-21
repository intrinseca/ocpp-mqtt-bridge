from datetime import time

import pytest
from zoneinfo import ZoneInfo

from ocpp_mqtt_bridge.util import today_at


def test_next_datetime_same_day_winter(patch_datetime_now):
    target_time = time(0, 30, tzinfo=ZoneInfo("Europe/London"))

    result = today_at(target_time).isoformat()

    assert result == "2024-01-02T00:30:00+00:00"


def test_next_datetime_same_day_summer(patch_datetime_now_summer):
    target_time = time(0, 30, tzinfo=ZoneInfo("Europe/London"))

    result = today_at(target_time).isoformat()

    assert result == "2024-07-01T23:30:00+00:00"


def test_dst_transition(patch_datetime_now_dst):
    target_time = time(0, 30, tzinfo=ZoneInfo("Europe/London"))

    result = today_at(target_time).isoformat()

    assert result == "2024-03-31T00:30:00+00:00"

    target_time = time(5, 30, tzinfo=ZoneInfo("Europe/London"))

    result = today_at(target_time).isoformat()

    assert result == "2024-03-31T04:30:00+00:00"


if __name__ == "__main__":
    pytest.main()
