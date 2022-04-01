def main(fruits1, fruits2):
    """
    You will be given a list of several fruits called fruits1 and fruits2. Return the result by adding the second to the first list.
    Args:
        fruits1(list): parameter
        fruits2(list): parameter
    Returns:
        list: return answer
    """
    fruits1.extend(fruits2)
    return fruits1


print(main(fruits1=["apple", "banana"], fruits2=["kiwi", "pear"]))
