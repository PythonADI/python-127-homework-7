def squares(n):
    a = []


    for i in range(1, n + 1):
        a.append(i * i)
    return a

def shout_all(words):

    a = []

    for i in words:
        a.append(i.upper() + "!")
    return a

print(squares(5))
print(squares(1))
print(squares(0))
print(shout_all(["hi", "bye", "wow"]))
print(shout_all([]))