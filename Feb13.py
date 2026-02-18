#1
print("Hello")
#2
age = 16
print(f"{age}")
#3
age = 17
print(f"{age}")
#4
a = 8
b = 3
print(f"{a} + {b}")
print(f"{a} - {b}")
print(f"{a} * {b}")
#5
print(f"{a} / {b}")
print(f"{a} // {b}")
print(f"{a} % {b}")
#6
radius = 4.5
pi = 3.14159
area = (radius ** 2) * pi
print(f"{area}")
#7
withoutparenth = 3 + 4 * 2
withparenth = (3 + 4) * 2
print(f"{withoutparenth}")
print(f"{withparenth}")
#8
first_name = "Ada"
last_name = "Lovelace"
print(f"{first_name} {last_name}")
#9
was = "was"
a = "a"
pioneer = "pioneer"
full_sentence = f"{first_name} {last_name} {was} {a} {pioneer}"
print(f"{full_sentence}")
#10
is_student = True
print(f"{is_student}")
#11
x = 10
y = 7
print(f"{x} > {y}")
print(f"{x} < {y}")
print(f"{x} == {y}")
print(f"{x} != {y}")
#12
print(f"{x} >= 10")
print(f"{y} <= 6")
#13
age = 18
has_ticket = True
print(f"{age} >= 18 and {has_ticket}")
#14
has_ticket = False
print(f"{age} >= 18 or {has_ticket}")
#15
print(f"not {has_ticket}")
#16
temperature = 72
is_raining = False
if temperature > 70 and is_raining == False:
    print("it is good picnic weather")
#17
score1 = 85
score2 = 92
average = (score1 + score2) / 2
if average > 90:
    print("average is above 90")
else:
    print("average is not above 90")
#18
is_higher = score1 > score2
question = "Is Score1 higher?"
q_a = f"{question} {not is_higher}"
print(f"{q_a}")
#19
gpa = 3.6
has_recommendation = True
if gpa >= 3.5 and has_recommendation == True:
    print("The Student Qualifies")
#20
equation1 = (5 * 2)
equation2 = (10 / 2)
if equation1 > 9 and equation2 == 5:
    print(f"{equation1} > 9 and {equation2} == 5")
#21
truth = True
lie = False
both = truth + lie
print(f"{both}")
#That number appears because of the boolean values of True and False are 1 and 0 in binary, and 1 + 0 is 1
#22
price = 19.999
add = 0.001
total = price + add
sentence =f"The Total is ${total}0"
print(f"{sentence}")
#23
name = "Marcus"
apples = 4
oranges = 6
total_fruit = apples + oranges
fruit_sentence = f"{name} had {total_fruit} pieces of fruit."
print(f"{fruit_sentence}")
#24
age = 20
citizen = True
registered = False
if age >= 18 and citizen == True and registered == True:
    print("This person can vote.")
else:
        print("This person cannot vote.")
#25
length = 10
width = 15
cost_per_square_unit = 5
Area = length * width
cost_per_unit = cost_per_square_unit
total_cost = Area * cost_per_unit
print(f"Length: {length}\nWidth: {width}\nArea: {Area}\nCost per unit: {cost_per_unit}\nTotal cost: {total_cost}")
if total_cost > 500:
    print("Price is over $500")
else:
    print("Price is not over $500")
#Interesting
t = "17"
print(t + "1")