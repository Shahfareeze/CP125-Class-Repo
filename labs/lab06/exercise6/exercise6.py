def manage_roster(enrolled, drop_requests, waitlist):
    """
    Processes student drop requests and adds from waitlist if needed.
    
    Args:
        enrolled: Set of currently enrolled student names
        drop_requests: List of student names requesting to drop
        waitlist: Set of students on the waitlist
    
    Returns:
        int: Count of final enrolled students
    """

    after_drop = set()
    for students in enrolled:
        if students not in drop_requests:
            after_drop.add(students)

    if len(after_drop) < 5:
        while len(after_drop) < 7 and len(waitlist) > 0:
           after_drop.add(waitlist.pop())

    return len(after_drop)

    
    pass
