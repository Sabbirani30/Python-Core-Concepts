

Friends = ["Anik", "Shifad", "Tamim", "Rohan", "Nabibl", "Fahad"]

for Friend in Friends:
    print(Friend)

# Break statement
Friends = ["Anik", "Shifad", "Tamim", "Rohan", "Nabibl", "Fahad"]

for Friend in Friends:
    if Friend == "Rohan":
        break
    print(Friend)


 # Continue Statement


Friends = ["Anik", "Shifad", "Tamim", "Rohan", "Nabibl", "Fahad"]
for Friend in Friends:
    if Friend == "Rohan":
        continue
    print(Friend)

# Range (range(stop))

for Number in range(11):
    print(Number)

for Numbers in range(9):

    if Numbers==5:
        break
    print(Numbers)
