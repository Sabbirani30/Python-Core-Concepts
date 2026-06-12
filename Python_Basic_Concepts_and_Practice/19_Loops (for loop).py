

Friends = ["Anik", "Shifad", "Tamim", "Rohan", "Nabibl", "Fahad"]

for Friend in Friends:
    print(Friend)


numbers = [10, 5, 20, 8, 30]

for n in numbers:
    if n > 15:
        print( f"{n} Big Number ")
    else:
        print(f"{n} Small Number ")


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

 # Range (range( start, stop)

for Digit in range(10,35):
    print(Digit)

for Digit in range(10,35):
    if Digit==32:
        break
    print(Digit)

for Digit in range(10,35):
    if Digit==32:
        continue
    print(Digit)


Anik= [1,2,3,4,5,6,7,8,9]
for number in Anik:
    if number==8:
        print(number)
        break

