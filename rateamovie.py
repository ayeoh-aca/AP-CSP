print("*** Welcome to Movie Rating App ***")
movies_watched = []
answer = ""
while answer != "done".lower():
    answer = input("Enter a movie title (or 'done' to finish): ")
    if answer != "done".lower():
        movies_watched.append(answer)
if movies_watched == []:
    print("No movies entered. Goodbye!")
else:
    print("--- Your Movie List ---")
    for movie in range(len(movies_watched)):
        print(f"{movie + 1}. {movies_watched[movie]}")
ratings = []
rating = 0
print("--- Rate Each Movie (1 = worst, 5 = best) ---")
for i in movies_watched:
    while True:
        rating = int(input(f"Your rating for {i}: "))
        if rating <= 5 and rating >= 1:
            break
        else:
            print("Please enter a numbber from 1 to 5")
    ratings.append(rating)
    if rating == 5: 
        print(" Excellent!")
    elif rating == 3 or 4:
        print(" Solid.")
    else:
        print(" Rough.")
print("--- This Week’s Stats ---")
average = 0
sm = 0
for rating in ratings:
    sm = sm + rating
average = sm/len(ratings)
print(f"Number of movies: {len(movies_watched)}")
print(f"Average rating: ({round(average, 1)} / 5)")
if average >= 4.0:
    print("Grade: A - Great taste!")
elif average >= 3.0:
    print("Grade: B - Solid week.")
elif average >= 2.0:
    print("Grade: C - Mixed bag.")
else:
    print("Grade: D - Rough week.")
print("--- Full Weekly Report ---")
label = ""
for i in range(len(movies_watched)):
    if ratings[i] == 5:
        label = "Must Watch"
    elif ratings[i] == 4:
        label = "Great Pick"
    elif ratings[i] == 3:
        label = "It Was Fine"
    else:
        label = "Skip It"
    print(f"{i + 1}. {movies_watched[i]} ({ratings[i]}/5) - {label}")
best_index = 0
worst_index = 0
for i in range(len(ratings)):
    if ratings[i] > ratings[best_index]:
        best_index = i
for i in range(len(ratings)):
    if ratings[i] < ratings[worst_index]:
        worst_index = i
if best_index != worst_index:
    print(f"Best movie: {movies_watched[best_index]} ({ratings[best_index]} / 5)")
    print(f"Worst movie: {movies_watched[worst_index]} ({ratings[worst_index]} / 5)")
else:
    print("Every movie got the same rating this week.")