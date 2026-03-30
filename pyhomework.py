#1.
"""balance = 0
while balance < 150:
    amount = int(input("Insert coins (in cents): "))
    balance = amount + balance
    if balance < 150:
        x = 150 - balance
        print(f"You still need {x} cents.")
print("Enjoy your snack!")
change = balance - 150
if change > 0:
    print(f"Change owed: {change} cents")
#2.
goal = int(input("How many reps is your goal? "))
reps = 0
while reps < goal:
    input("Press enter to log a rep: ")
    reps = reps + 1
    print(f"Reps done: {reps}/{goal}")
print("Set complete! GREAT WORK.")
#3.
correct_pin = "4821"
attempts = 0
guess = ""
while attempts < 3 and guess != correct_pin:
    guess = input("Enter PIN: ")
    attempts = attempts + 1
    remain = 3 - attempts
    if guess != correct_pin:
        print(f"Incorrect. You have {remain} attempt(s) remaining")
if guess == correct_pin:
    print("Access granted!")
else:
    print("Account locked. Too many failed attempts")
#4.
songs = []
answer = ""
while answer != "done".lower():
    answer = input("Add a song (or type 'done' to finish): ")
    if answer != "done".lower():
        songs.append(answer)
if songs == "":
    print("No songs added.")
else:
    print("Your Playlist: ")
    for song in range(len(songs)):
        print((song+1), (songs[song]))
#5.
fridge = []
ingredient = ""
while ingredient != "done".lower():
    ingredient = input("Enter an ingredient (or 'done' to finish): ")
    if ingredient != "done".lower():
        fridge.append(ingredient)
needed = ["eggs", "butter", "milk"]
haveeggs = 0
havebutter = 0
havemilk = 0
haveall = 0
for item in range(len(fridge)):
    if fridge[item] == "eggs" and haveeggs == 0:
        print("eggs ... HAVE IT")
        haveall = haveall +1
        haveeggs = 1
    if fridge[item] == "butter" and havebutter == 0:
        print("butter ... HAVE IT")
        haveall = haveall +1
        havebutter = 1
    if fridge[item] == "milk" and havemilk == 0:
        print("milk ... HAVE IT")
        haveall = haveall +1
        havemilk = 1
if haveeggs == 0:
    print("eggs ... MISSING")
if havebutter == 0:
    print("butter ... MISSING")
if havemilk == 0:
    print("milk ... MISSING")
if haveall == 3:
    print("You can make scrambled eggs!")
else:
    print("You are missing ingredients.")
#6.
prices = []
value = 0
total = 0
tip_amount = 0
while value != -1:
    value = float(input("Enter a meal price (or -1 to finish): "))
    if value != -1:
        prices.append(value)
for price in range(len(prices)):
    total = total + prices[price]
print(f"Table total: ${total:.2f}")
tip_rates = [0.10, 0.15, 0.18, 0.20]
for tip in range(len(tip_rates)):
    tip_amount = total * tip_rates[tip]
    final_total = total + tip_amount
    print(f"{tip_rates[tip]*100:.2f}% tip: ${tip_amount:.2f} tip ---> ${final_total:.2f} total")
#7."""
steps = []
day = 1
while len(steps) != 7:
    track = int(input(f"Enter steps for day {day}: "))
    if len(steps) != 7:
        steps.append(track)
greater = 0
for step in range(len(steps)):
    if steps[step] > greater:
        steps


