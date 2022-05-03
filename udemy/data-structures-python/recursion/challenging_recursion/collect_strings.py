def collectStrings(obj):
    result = []
    for key, value in obj.items():
        if isinstance(value, str):
            result.append(value)
        if isinstance(value, dict):
            result.extend(collectStrings(value))
    return result