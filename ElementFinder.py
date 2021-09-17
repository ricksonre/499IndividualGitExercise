def find(number,elements):
    # Find if a element is present in a array. Returns true if found, false otherwise.
    for element in elements:
        if element == number:
            return True
    return False