#1.
balance = 0
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
#7.
steps = []
while len(steps) < 7:
    day = len(steps) + 1
    track = int(input(f"Enter steps for day {day}: "))
    if len(steps) < 7:
        steps.append(track)
best = steps[0]
best_index = 0
for i in range(len(steps)):
    if steps[i] > best:
        best = steps[i]
        best_index = i
    
for term in range(7):
    print(f"Day {day+1}: {steps[term]} steps")
    if steps[term] >= 10000:
        print("Goal met!")
    else:
        print(f"{10000-steps[term]} steps short")
print(f"Best day: Day {best_index+1} with {best} steps.")
#8.
movies = ["Inception", "Clueless", "Parasite", "Get Out"]
votes = [0, 0, 0, 0]
answer = 1
for i in range(4):
    print(f"{i+1}. {movies[i]}")
while answer != 0:
    answer = int(input("Enter a number 1-4 to vote, or 0 to close voting: "))
    if 1 <= answer <= 4:
        votes[answer - 1] += 1
    else:
        print("Invalid choice")
for i in range(4):
    print(f"{movies[i]}: {votes[i]} votes")
highest = votes[0]
for i in range(4):
    if votes[i] > highest:
        highest = i
count = 0
win = 0
for i in range(4):
    if votes[i] == highest:
        count += 1
        win = i
if count == 1:
    print(f"Winner: {movies[win]}!")
else:
    print("It's a tie.")
#9.
budget = float(input("What is your total budget? $"))
limit = float(input("What is your per-item spending limit? $"))
names = []
costs = []
name = ""
cost = 0
while name != "done":
    name = input("Item name (or done to finish): ")
    if name == "done":
        break
    else:
        cost = float(input("Cost of that item: $"))
    names.append(name)
    costs.append(cost)
total = 0
for i in range(len(costs)):
    total = total + costs[i]
for i in range(len(names)):
    print(f"{names[i]} costs {costs[i]:.2f}")
    if costs[i] > limit:
        print("This item exceeded your per-item limit.")
for i in range(len(names)):
    print(f"{i+1}. {names[i]} - ${costs[i]:.2f} ({(costs[i]/total)*100:.1f}% of total)")
if total > budget:
    print(f"Over budget by ${total-budget:.2f}")
else:
    print(f"Under budget. ${budget-total:.2f} remaining.")