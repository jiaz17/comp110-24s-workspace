"""EX05_Dictionary."""
__author__ = "730679888"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values."""
    inverted_dict = {}
    for key, value in input_dict.items():
        if value in inverted_dict:
            raise KeyError("error message of your choice here!")
        inverted_dict[value] = key
    return inverted_dict


def favorite_color(color_dict: dict[str, str]) -> str:
    """Find the most popular color's names and favorite colors."""
    color_count: dict[str, int] = {}
    for color in color_dict.values():
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
    max_count = max(color_count.values())
    for name, color in color_dict.items():
        if color_count[color] == max_count:
            return color
    return ""


def count(items: list[str]) -> dict[str, int]:
    """Counts the frequency of each string."""
    result_dict: dict[str, int] = {}
    for item in items:
        if item in result_dict:  
            result_dict[item] += 1 
        else:  
            result_dict[item] = 1 
    return result_dict


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Categorizes a list of words."""
    result_dict = {}
    for word_name in words:
        word_lower = word_name.lower()
        key = word_lower[0]
        if key not in result_dict:
            result_dict[key] = [word_name]
        else:
            result_dict[key].append(word_name)
    return result_dict


def update_attendance(attendance_log: dict[str, list[str]], day: str, student: str) -> None:
    """Updates the attendance log dictionary with a new student."""
    if day not in attendance_log:
        attendance_log[day] = []
    attendance_log[day].append(student)