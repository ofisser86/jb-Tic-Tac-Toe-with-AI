def object_with_beautiful_identity():
    for i in range(10_000):
        # Change the next line
        if '888' in str(id(i)):
            return i
    return None
