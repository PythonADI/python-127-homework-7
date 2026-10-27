def first_negative(numbers):
    for i in numbers:
        if i < 0:
            return i
    return None

def count_above(numbers, limit):
    count = 0

    for i in numbers:
        if i >= limit:
            count += 1

    return count

def warmest_day(temps):
    a = 0

    for i in range(len(temps)):
        if temps[i] > temps[a]:
            a = i
    return a

temps = [3, -2, 5, -7, 8, 1]

print(first_negative(temps))
print(first_negative([4, 5]))
print(count_above(temps, 2))
print(warmest_day(temps))
print(warmest_day([9, 2, 9]))