def first_negative(numbers):
    """Return the first negative number or None if there is none."""
    for number in numbers:
        if number < 0:
            return mumber
        return None
def count_above(numbers,limit):
    """Return how many numbers are greater than the Limit."""
    count = 0
    for number in numbers:
        if number > limit:
            count += 1
    return count


def warmest_day(temps):
    """Return the index of the first highest temperature."""
    warmest = 0
    for i in range(len(temps)):
        if temps[i] > temps[warmest]:
            warmest = i
    return warmest
temps = [3, -2, 5, -7, 8, 1]
print(first_negative(temps))
print(first_negative([4, 5]))
print(count_above(temps, 2))
print(warmest_day(temps))
print(warmest_day([9, 2, 9]))