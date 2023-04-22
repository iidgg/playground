scores = []
length = 0

while True:
    try:
        n = int(input("How many scores: "))
        if n > 0:
            length = n
            break
    except ValueError:
        print("bruh, i need a NUMBER!")

while True:
    if len(scores) >= length:
        break
    try:
        n = int(input(f"score {len(scores) + 1}: "))
        scores.append(n)
    except ValueError:
        print("bruh, i need a NUMBER!")

avg = sum(scores) / len(scores)
print(f"avg: {avg}")
