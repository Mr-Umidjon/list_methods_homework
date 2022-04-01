def main(fruits):
    """
    A list called “fruits” is given and is five in length and contains at least one “apple”. Calculate how many “apple” were involved and return the indexes in a list view.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    count = [fruits.count('apple')]
    if count[0] == 0:
        return count
    i = 0
    if fruits[i] == 'apple':
        count.append(i)
    i += 1

    if fruits[i] == 'apple':
        count.append(i)
    i += 1

    if fruits[i] == 'apple':
        count.append(i)
    i += 1

    if fruits[i] == 'apple':
        count.append(i)
    i += 1

    if fruits[i] == 'apple':
        count.append(i)
    i += 1
    return count


print(main(fruits=["apple", "apple", "apple", "apple", "kiwi"]))
print(main(fruits=["apple", "banana", "apple", "pear", "apple"]))
