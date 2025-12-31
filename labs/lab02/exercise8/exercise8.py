def calculate_bounce_height(current_height):
    """Calculate next bounce height (80% of current)."""
    # TODO: Implement this function
    height = 0.8 * current_height
    return height

def is_ball_stopped(height):
    """Return True if height < 1, False otherwise."""
    # TODO: Implement this function
    if height > 1:
        return True 
    else: 
        return False

def calculate_bounce_count(initial_height):
    """
    Count how many times the ball bounces.
    """
    # TODO: Implement using calculate_bounce_height and is_ball_stopped
    current_height = start_height
    height = calculate_bounce_height(current_height)
    bounce_count = 0 
    total_distance = start_height
    
    while is_ball_stopped(calculate_bounce_height(current_height)):
        height = calculate_bounce_height(current_height)
        total_distance += height *2
        bounce_count += 1

    return (bounce_count, total_distance)

    


# Test your code here
print("Testing Bouncing Ball Simulation...")
