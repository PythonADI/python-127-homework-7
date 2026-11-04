def squares(n):
    list_squares = []
    for num in range(1, n + 1):
        list_squares.append(num ** 2)
    return list_squares

def shout_all(words):
    shouted_words = []
    for member in words:
        shouted_words.append(member.upper() + "!")
    return shouted_words

print(squares(5))
print(squares(1))
print(squares(0))
print(shout_all(["hi", "bye", "wow"]))
print(shout_all([]))