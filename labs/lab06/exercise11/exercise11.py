def get_student_courses(enrollments, student_id):
    """Return set of courses this student has completed."""
    all_students = set()
    for student_id, course in enrollments:
        if student_id not in all_students:
            all_students.add(student_id)

    return all_students   
    pass

def find_missing_courses(completed_courses, required_courses):
    """Return set of required courses not yet completed."""
    pass

def build_student_report(students, enrollments, required_courses):
    """Return sorted list of tuples (missing_count, student_id) for students with missing courses."""
    pass

def find_incomplete_students(enrollments, required_courses):
    """Find students who haven't completed all required courses."""
    
    pass

def find_incomplete_students(enrollments, required_courses):
    """Find students who haven't completed all required courses."""
    all_students = []
    for student_id, course in enrollments:
        if student_id not in all_students:
            all_students.append(student_id)
    
    incomplete = []
    for student in all_students:
        completed = []
        for sid, course in enrollments:
            if sid == student and course not in completed:
                completed.append(course)
        
        missing = []
        for required in required_courses:
            if required not in completed:
                missing.append(required)
        
        if len(missing) > 0:
            incomplete.append((len(missing), student))
    
    return sorted(incomplete, reverse=True)