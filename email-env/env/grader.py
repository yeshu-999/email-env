def grade(task, action):
    expected = task["expected"]

    if task["name"] == "classification":
        return 1.0 if action == expected else 0.0

    if task["name"] == "reply":
        return 1.0 if expected.lower() in action.lower() else 0.5

    if task["name"] == "multi_step":
        return 1.0 if "schedule" in action.lower() else 0.5

    return 0.0