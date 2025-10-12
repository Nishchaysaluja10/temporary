def longest_positive_streak(nums: list[int]) -> int:
    """
    Returns the length of the longest run of consecutive values strictly greater than 0.
    Returns 0 for empty lists.
    Resets the count when encountering 0 or negative numbers.
    """
    if not nums:
        return 0

    max_streak = 0
    current_streak = 0
    for num in nums:
        if num > 0:
            current_streak += 1
        else:
            max_streak = max(max_streak, current_streak)
            current_streak = 0
    max_streak = max(max_streak, current_streak)
    return max_streak