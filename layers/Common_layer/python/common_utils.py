from datetime import datetime
from uuid import uuid4


def create_unique_id(prefix: str):
    return f"{prefix}-{datetime.now().strftime('%Y%m-%d-%H%M%S%f')}-{str(uuid4())}"
