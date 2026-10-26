shopping = ["bread", "milks", "egg"]
print("First:",shopping[0])
print("Last:", shopping[-1])


shopping[1] = "kefir"
print(shopping)

shopping.append("cheese")
print(shopping)

shopping.remove("egg")
print(shopping)
bought = shopping.pop()
print("Bought:", bought)
print(shopping)
print(len(shopping), "items")