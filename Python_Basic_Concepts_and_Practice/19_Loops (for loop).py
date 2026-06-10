

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
