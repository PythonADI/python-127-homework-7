shopping = ["bread", "milk", "eggs"]


print("first:", shopping[0])
print("last:", shopping[-1])


shopping[1] = "kefir"
shopping.append("cheese")
shopping.insert(0, "water")
shopping.remove("eggs")


item = shopping.pop()
print("Bought:", item)

print(shopping)

print(len(shopping), "items")