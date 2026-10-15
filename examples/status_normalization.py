"""Portfolio example only: standalone, synthetic, not production source."""
from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass(frozen=True)
class Telemetry:
    serial: str
    last_seen: datetime | None
    collection_enabled: bool


def collection_status(item: Telemetry, now: datetime) -> str:
    """A minimal illustrative status rule, not the REP-Monitor business policy."""
    if not item.collection_enabled:
        return "COLLECTION_DISABLED"
    if item.last_seen is None:
        return "NO_READING"
    if item.last_seen.tzinfo is None or now.tzinfo is None:
        raise ValueError("Timezone-aware datetimes are required")
    delta = now - item.last_seen
    if delta.total_seconds() < 0:
        return "INVALID_FUTURE_TIMESTAMP"
    return "STALE" if delta.days >= 7 else "COLLECTING"


if __name__ == "__main__":
    sample = Telemetry(
        serial="DEMO-0001",
        last_seen=datetime(2026, 1, 1, tzinfo=timezone.utc),
        collection_enabled=True,
    )
    print(collection_status(sample, datetime(2026, 1, 10, tzinfo=timezone.utc)))
