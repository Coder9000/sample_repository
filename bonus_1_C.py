marks = [78, 81, 45, 91, 85, 79, 63, 86, 67, 96, 52, 60, 81, 83, 65, 71, 90]

def get_average(marks):
    numerator = 0
    
    for num in range(len(marks)):
        numerator += marks[num]
    
    return (numerator/(num + 1))

def get_medium(marks):
    return (sorted(marks)[int((len(marks) - 1) / 2)])

print(get_average(marks))
print(get_medium(marks))
