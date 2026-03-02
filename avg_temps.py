def avg_temps(temps: list):
    sum = 0
    count = 0
    for temp in temps:
        sum += temp
        count += 1
    return sum/count
print(avg_temps([1,2,3,4,5,6,7,8,9,10]))
