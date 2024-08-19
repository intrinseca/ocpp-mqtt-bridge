import datetime
from datetime import time, timedelta

import pytest
import pytz

from ocpp_mqtt_bridge.util import next_datetime_at_time


def test_next_datetime_same_day(patch_datetime_now):
    target_time = time(14, 30)  # 2:30 PM London time, later today
    result = next_datetime_at_time(target_time)

    # The expected result should be today at 2:30 PM in UTC
    expected_time = (
        pytz.timezone("Europe/London")
        .localize(
            datetime.datetime.combine(datetime.datetime.now().date(), target_time)
        )
        .astimezone(pytz.utc)
    )

    assert result == expected_time


def test_next_datetime_next_day(patch_datetime_now):
    target_time = time(8, 0)  # 8:00 AM London time, earlier today
    result = next_datetime_at_time(target_time)

    # The expected result should be tomorrow at 8:00 AM in UTC
    expected_time = (
        pytz.timezone("Europe/London")
        .localize(
            datetime.datetime.combine(
                datetime.datetime.now().date() + timedelta(days=1), target_time
            )
        )
        .astimezone(pytz.utc)
    )

    assert result == expected_time


def test_midnight_transition(patch_datetime_now):
    target_time = time(0, 0)  # Midnight
    result = next_datetime_at_time(target_time)

    london_tz = pytz.timezone("Europe/London")

    if datetime.datetime.now().time() > target_time:
        # If it's past midnight today, the result should be tomorrow's midnight in UTC
        expected_date = datetime.datetime.now().date() + timedelta(days=1)
    else:
        # Otherwise, it should be today's midnight in UTC
        expected_date = datetime.datetime.now().date()

    expected_time = london_tz.localize(
        datetime.datetime.combine(expected_date, target_time)
    ).astimezone(pytz.utc)

    assert result == expected_time


if __name__ == "__main__":
    pytest.main()
