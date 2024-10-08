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
        raise ValueError("Invalid time input")
    
    # Convert 24-hour format to 12-hour format
    hours = hours % 12
    
    # Calculate angles
    hour_angle = (hours + minutes / 60) * 30  # 360 degrees / 12 hours = 30 degrees per hour
    minute_angle = minutes * 6  # 360 degrees / 60 minutes = 6 degrees per minute
    
    # Calculate the difference and ensure it's the smaller angle
    angle_diff = abs(hour_angle - minute_angle)
    return min(angle_diff, 360 - angle_diff)