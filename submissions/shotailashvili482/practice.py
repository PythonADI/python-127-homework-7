#exercise - sort

places = ['afghanistan', 'kongo', 'nigeria', 'pakistan', 'bangladesh']
print(places)
print(sorted(places))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse = True)
print(places)



#exercise - lists

guests = ['avtandil', 'pridon', 'tariel', 'rostevan', 'giorgi']

1
def invite():
  for person in guests:
    print(f"I invite you on my birthday party,{person}!")
  print(f"guests invited: {len(guests)}")
invite()


#2
rejected = [guests.pop(guests.index('avtandil')), guests.pop(guests.index('rostevan'))]
print(f"Unfortunately, {rejected[0]} and {rejected[1]}, cannot come.")
print("Instead, lamara and zaza will come!\n")
guests.insert(0, 'lamara')
guests.insert(3, 'zaza')
invite()


#3
print(f"\nI found a bigger dinner table, I can invite more people!")
guests.insert(0, 'jumbera')
guests.insert(3, 'valeri')
guests.append('gurandukht')
invite()


#4
print("\nUnfortunately, new dinner table won't be ready on time, i can only invite two guests.")
while len(guests) > 2:
  not_invited = guests.pop()
  print(f"Sorry, {not_invited}, not enough space.")
invite()


#5
del guests[:]
print(f"\nguests arrived: {len(guests)}")



# exercise 2 - lists

participants = []
print("Whoever wants to participate, sign up down below!")

while len(participants) < 4:
  name = input("type name: ")
  participants.append(name)
print(f"Participants: {', '.join(participants)}")

# exercise - game

line = ['✨', '✨', '✨', '😎', '✨', '✨']
print(line)

while True:
    direction = input("Move: ").lower().strip()

    position = line.index('😎')

    if direction == "right" and position < len(line) - 1:
      line.pop(position)
      line.insert(position + 1, '😎')
      print(line)
    elif direction == "left" and position > 0:
      line.pop(position)
      line.insert(position - 1, '😎')
      print(line)
    if direction == "quit":
      break

# exercise - game 2d                                                          ეს ვერ გავაკეთე!

line = [['✨', '✨', '✨', '😎', '✨', '✨'],
        ['✨', '✨', '✨', '✨', '✨', '✨'],
        ['✨', '✨', '✨', '✨', '✨', '✨'],
        ['✨', '✨', '✨', '✨', '✨', '✨'],
        ['✨', '✨', '✨', '✨', '✨', '✨'],
        ['✨', '✨', '✨', '✨', '✨', '✨']]
def display():
  for row in line:
    print(''.join(row))
while True:
    direction = input("Move: ").lower().strip()
    for member in line:
      

    if direction == "right" and position < len(line) - 1:
      line.pop(position)
      line.insert(position + 1, '😎')
      display()
    elif direction == "left" and position > 0:
      line.pop(position)
      line.insert(position - 1, '😎')
      display()
    elif direction == "quit":
      break
    else:
      print("Invalid Command! use left, right or quit")



    