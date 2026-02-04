def get_unique_attendees(attendance_logs):
    """Extract set of all unique attendee IDs."""
    pass

def count_unique_events(attendance_logs, attendee_id):
    """Count how many unique events this attendee attended."""
    pass

def filter_by_threshold(attendees, attendance_logs, min_events):
    """Return sorted list of attendees who attended >= min_events."""
    pass

def find_frequent_attends(attendance_logs, min_events):
    """Find attendees who attended at least min_events unique events."""
    
    pass



def find_frequent_attendees(attendance_logs, min_events):
    """Find attendees who attended at least min_events unique events."""
    all_attendees = []
    for attendee_id, event_name in attendance_logs:
        if attendee_id not in all_attendees:
            all_attendees.append(attendee_id)
    
    qualified = []
    for attendee_id in all_attendees:
        events_attended = []
        for att_id, event_name in attendance_logs:
            if att_id == attendee_id and event_name not in events_attended:
                events_attended.append(event_name)
        
        if len(events_attended) >= min_events:
            qualified.append(attendee_id)
    
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