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
area = 2 * radius * pi
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
