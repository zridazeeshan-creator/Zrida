# ==========================================
# TASK 1: Number Guessing Countdown
# ==========================================
# TEST RUN 1: Input: -2, then 3
# TEST RUN 2: Input: 5

num = int(input("Enter a number: "))

# Keep asking if negative
while num <= 0:
    print("Must be positive!")
    num = int(input("Enter a number: "))

# Countdown
while num > 0:
    print(num)
    num = num - 1

print("Liftoff!")


# ==========================================
# TASK 2: Student Grade Dictionary
# ==========================================
# TEST RUN 1: Default dictionary output
# TEST RUN 2: Tested with {"John": 90, "Mark": 40}

students = {"Ali": 85, "Sara": 42, "Bilal": 67, "Hina": 91, "Zara": 55}
total = 0

for name in students:
    score = students[name]
    total = total + score
    
    if score >= 90:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"
        
    print(name, ":", grade)

print("Average:", total / len(students))


# ==========================================
# TASK 3: Coordinate Distance Checker
# ==========================================
# TEST RUN 1: Default points output
# TEST RUN 2: Tested with [(1,1), (5,5)]

points = [(2, 3), (5, 7), (-1, -1), (0, 0), (4, 4)]

closest = points[0]
min_dist = 9999

for p in points:
    # formula: sqrt(x^2 + y^2)
    dist = (p[0]**2 + p[1]**2) ** 0.5
    print("Point", p, "Distance:", round(dist, 2))
    
    if dist < min_dist:
        min_dist = dist
        closest = p

print("Closest point:", closest)


# ==========================================
# TASK 4: Inventory Manager
# ==========================================
# TEST RUN 1: Inputs: pen, exit
# TEST RUN 2: Inputs: eraser, exit

inventory = {"pen": 10, "notebook": 5, "eraser": 0, "sharpener": 8}

item = ""
while item != "exit":
    item = input("Enter item name (or 'exit'): ").lower()
    
    if item == "exit":
        print("Goodbye!")
    elif item in inventory:
        if inventory[item] > 0:
            inventory[item] = inventory[item] - 1
            print("Remaining stock:", inventory[item])
        else:
            print("Out of stock")
    else:
        print("Item not found")


# ==========================================
# TASK 5: Word Frequency Counter
# ==========================================
text = input("Enter sentence: ")
words = text.lower().split()

counts = {}
for w in words:
    # Remove punctuation like periods or commas from edges
    w = w.strip(".,!?")
    
    if w in counts:
        counts[w] = counts[w] + 1
    else:
        counts[w] = 1

print("\nWord Frequencies:")
for w in counts:
    print(w, ":", counts[w])

# Convert dictionary to a list of tuples (word, count)
pairs = []
for w in counts:
    pairs.append((w, counts[w]))

# Sort by count from highest to lowest
for i in range(len(pairs)):
    for j in range(len(pairs) - 1):
        if pairs[j][1] < pairs[j + 1][1]:
            pairs[j], pairs[j + 1] = pairs[j + 1], pairs[j]

print("\nTop 3 Words:")
print(pairs[:3])