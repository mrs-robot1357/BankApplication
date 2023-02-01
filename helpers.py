def verify_type_or_raise_error(value, expected_type):
    if not isinstance(value, expected_type):
        raise TypeError(f"Please provide an object of class {expected_type} not a {type(value)}")
    return value