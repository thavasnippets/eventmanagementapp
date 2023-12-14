from datetime import datetime, timezone


def get_datetime_from_timestamp(timestamp):
    return (datetime.fromtimestamp(timestamp/1000.0).replace(tzinfo=timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ"))


def get_current_timestamp():
    current_datetime = datetime.now(timezone.utc)
    utc_time = current_datetime.replace(tzinfo=timezone.utc)
    return utc_time.timestamp()


def get_current_datetime():
    return datetime.now(timezone.utc).strftime("%Y-%m-dT%H:%M:%S.%fZ")
