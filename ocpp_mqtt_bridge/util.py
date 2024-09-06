import datetime

from zoneinfo import ZoneInfo


def today_at(target_time: datetime.time) -> datetime.datetime:
    # Define the timezones

    london_tz = ZoneInfo("Europe/London")
    now = datetime.datetime.now(london_tz)

    # Create a datetime object for 00:30 today in the London timezone
    result = datetime.datetime.combine(now, target_time)

    # Convert the target time to UTC
    utc_time = result.astimezone(datetime.UTC)

    return utc_time
