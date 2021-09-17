
def count(element, array):
    # Find how many times an element is repeated in an array. And repeats the count
    count = 0
    for e in array:
        if element == e:
            count += 1
    return count