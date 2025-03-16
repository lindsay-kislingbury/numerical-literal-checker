def hexadecimal_integer_checker(input_str):  # linds

    # reject empty strings
    if not input_str:
        return False

    # reject strings too short to be valid hexadecimal integers
    if len(input_str) < 3:
        return False

    # reject strings that don't start with '0x' or '0X'
    if input_str[:2] not in ["0x", "0X"]:
        return False

    # reject strings that end with _ or contain double _
    after_prefix = input_str[2:]
    if after_prefix.endswith("_") or "__" in after_prefix:
        return False

    # reject strings that contain invalid characters
    # valid characters are 0-9, a-f, A-F, and _
    for char in input_str[2:]:
        if char not in "0123456789abcdefABCDEF_":
            return False

    # if all checks pass, return True
    return True
