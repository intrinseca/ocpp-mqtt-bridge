import datetime

import pytz


def next_datetime_at_time(target_time: datetime.time) -> datetime.datetime:
    # Define the timezones
    london_tz = pytz.timezone("Europe/London")
    utc_tz = pytz.utc

    # Get the current time in the London timezone
    now = datetime.datetime.now(london_tz)

    # Combine the current date with the target time in the London timezone
    today_target = datetime.datetime.combine(now.date(), target_time).astimezone(
        london_tz
    )

    if now > today_target:
        # If the target time has already passed today,
        # return the target time for tomorrow
        next_target = today_target + datetime.timedelta(days=1)
    else:
        # Otherwise, return the target time for today
        next_target = today_target

    # Convert the result to UTC
    return next_target.astimezone(utc_tz)
