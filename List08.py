def main(fruits):
    """
    A list called "fruits" is given and is five in length and contains at least one "apple". Remove the apples from the list and return the list.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    if fruits.count('apple'):
        fruits.pop(fruits.index('apple'))

    if fruits.count('apple'):
        fruits.pop(fruits.index('apple'))

    if fruits.count('apple'):
        fruits.pop(fruits.index('apple'))

    if fruits.count('apple'):
        fruits.pop(fruits.index('apple'))

    if fruits.count('apple'):
        fruits.pop(fruits.index('apple'))
    return fruits


print(main(["apple", "apple", "apple", "apple", "kiwi"]))
