def get_unique_attendees(attendance_logs):
    """Return a list of unique attendee IDs."""
    attendees = set()
    for attendee_id, event_name in attendance_logs:
        if attendee_id not in attendees:
            attendees.add(attendee_id)
    return attendees


def count_unique_events(attendance_logs, attendee_id):
    """Count unique events attended by a specific attendee."""
    events = set()
    for att_id, event_name in attendance_logs:
        if att_id == attendee_id and event_name not in events:
            events.add(event_name)
    return len(events)


def filter_by_threshold(attendees, attendance_logs, min_events):
    """Filter attendees who attended at least min_events unique events."""
    qualified = []
    for attendee_id in attendees:
        if count_unique_events(attendance_logs, attendee_id) >= min_events:
            qualified.append(attendee_id)
    return qualified


def find_frequent_attendees(attendance_logs, min_events):
    """Find attendees who attended at least min_events unique events."""
    attendees = get_unique_attendees(attendance_logs)
    qualified = filter_by_threshold(attendees, attendance_logs, min_events)
    return sorted(qualified)

attendance_logs = [
    ("A1", "Workshop_Python"),
    ("A1", "Workshop_Data"),
    ("A2", "Workshop_Python"),
    ("A1", "Workshop_Python"),  # duplicate
    ("A3", "Workshop_Data"),
    ("A2", "Workshop_Data"),
    ("A2", "Workshop_Web")
]

print(find_frequent_attendees(attendance_logs, 2))