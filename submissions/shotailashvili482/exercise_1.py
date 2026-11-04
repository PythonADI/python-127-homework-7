shopping = ["bread", "milk", "eggs"]
print(f"First: {shopping[0]}")
print(f"Last: {shopping[-1]}")

shopping[1] = "kefir"
shopping.append("cheese")
shopping.insert(0, "water")
shopping.remove("eggs")
bought = shopping.pop()
print(f"Bought: {bought}")
print(shopping)
print(f"{len(shopping)} items")