# Exercises

Create these files inside your own folder:
`submissions/<your-github-username>/`.

Give every function you write a one-line docstring saying what it
returns or does.

## exercise_1.py — Shopping list

Start with exactly this list:

```python
shopping = ["bread", "milk", "eggs"]
```

Then, in this order:

1. Print the first item and the last item. Use a **negative index**
   for the last one.
2. Replace `"milk"` with `"kefir"` by assigning to its index.
3. Add `"cheese"` to the end.
4. Insert `"water"` at the start.
5. Remove `"eggs"`.
6. Take the last item out with `pop()` and print `Bought: <item>`.
7. Print the list, then print how many items it has using `len()`.

Expected output:
```
First: bread
Last: eggs
Bought: cheese
['water', 'bread', 'kefir']
3 items
```

## exercise_2.py — Fix the bug

This code should print `42`, then the list **unchanged**, then `5`.
Instead it crashes with
`TypeError: 'NoneType' object is not subscriptable`. Copy it into
`exercise_2.py`, then fix the function. Change only the line with the
`BUG` comment.

```python
def highest(numbers):
    """Return the biggest number in the list."""
    ordered = numbers.sort()   # BUG: fix this line
    return ordered[-1]

nums = [7, 42, 19]
print(highest(nums))
print(nums)
print(highest([5]))
```

Expected output:
```
42
[7, 42, 19]
5
```

## exercise_3.py — Build a list

Write two functions. Each one starts with an empty list, appends to it
inside a loop, and returns it.

- `squares(n)` returns the squares of the numbers from 1 to `n`.
- `shout_all(words)` returns a **new** list with every word in upper
  case and a `!` on the end.

Then call them like this:

```python
print(squares(5))
print(squares(1))
print(squares(0))
print(shout_all(["hi", "bye", "wow"]))
print(shout_all([]))
```

Expected output:
```
[1, 4, 9, 16, 25]
[1]
[]
['HI!', 'BYE!', 'WOW!']
[]
```

## exercise_4.py — Temperatures

Write these three functions with loops. Do **not** use `.index()`,
`min()` or `max()` in this exercise.

- `first_negative(numbers)` returns the first number below zero, or
  `None` if there is none. Return early.
- `count_above(numbers, limit)` returns how many numbers are bigger
  than `limit`.
- `warmest_day(temps)` returns the **index** of the highest
  temperature. If two days tie, return the first one. Loop over
  `range(len(temps))`.

Then call them like this:

```python
temps = [3, -2, 5, -7, 8, 1]
print(first_negative(temps))
print(first_negative([4, 5]))
print(count_above(temps, 2))
print(warmest_day(temps))
print(warmest_day([9, 2, 9]))
```

Expected output:
```
-2
None
3
4
0
```

## exercise_5.py — Bonus: score report

Write a function `read_scores()` that keeps asking for scores and
**returns** them as a list of whole numbers. Each time it asks, it
first prints `Score (or done):` on its own line and then calls
`input()` with **no prompt text**. When the user types `done`, return
the list. (You may assume every other answer is a whole number.)

Write a second function `report(scores)` that prints three lines: the
scores in the order they were typed, the scores sorted from lowest to
highest, and the lowest, highest and average score — in exactly the
format shown below. If the list is empty, it prints `No scores.`
instead (return early).

Then use them like this:

```python
scores = read_scores()
report(scores)
```

Run it and type these five values, one per line, pressing Enter after
each: `8`, `3`, `10`, `5`, `done`.

Expected output, as it looks in the terminal (the lines `8`, `3`,
`10`, `5` and `done` are what you typed):
```
Score (or done):
8
Score (or done):
3
Score (or done):
10
Score (or done):
5
Score (or done):
done
Scores: [8, 3, 10, 5]
Sorted: [3, 5, 8, 10]
Lowest 3, highest 10, average 6.5
```

Run it a second time and type only `done`. Expected output:
```
Score (or done):
done
No scores.
```
