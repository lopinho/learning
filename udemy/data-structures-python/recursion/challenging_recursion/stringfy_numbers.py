def stringifyNumbers(obj):
    for key, value in obj.items():
        if isinstance(value, int) and value is not True:
            obj[key] = str(value)
        if isinstance(value, dict):
            stringifyNumbers(value)
    return obj