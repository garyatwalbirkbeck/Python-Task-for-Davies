def calculate_clock_angle(hours: int, minutes: int) -> float:
    """
    Calculate the angle between the hour and minute hands on a clock.
    
    Args:
        hours (int): The hour (0-23).
        minutes (int): The minutes (0-59).
    
    Returns:
        float: The angle between the hour and minute hands in degrees.
    
    Raises:
        ValueError: If the input hours or minutes are out of range.
    """
    if not (0 <= hours < 24 and 0 <= minutes < 60):
        raise ValueError("Invalid time input. Hours must be 0-23 and minutes must be 0-59.")
    
    # Convert 24-hour format to 12-hour format
    hours = hours % 12
    
    # Calculate the position of the hour hand
    hour_angle = (hours * 30) + (minutes * 0.5)
    # The hour hand moves 30 degrees per hour (360 / 12 = 30)
    # It also moves 0.5 degrees per minute (30 / 60 = 0.5)
    
    # Calculate the position of the minute hand
    minute_angle = minutes * 6
    # The minute hand moves 6 degrees per minute (360 / 60 = 6)
    
    # Calculate the angle between the hands
    angle = abs(hour_angle - minute_angle)
    
    # Return the smaller angle
    return min(angle, 360 - angle)