def squares(n):
    """Return a list of squares from 1 to n."""
    result = []
    for number in range(1, n + 1):
        result.append(number ** 2)
    return result


def shout_all(words):
    """Return uppercase words with an axclamation mark."""
    result = []
    for word in words:
        result.append(word.upper() + "!")
    return result
print(squares(5))
print(squares(1))
print(squares(0))
print(shout_all(["hi", "bye", "wow"]))
print(shout_all([]))