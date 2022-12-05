# Concept 1

a = [1, 2, 3, 4, 5, 6, 7, 8]

b = []

b.extend(a[-3:])

for i in range(3):
    a.pop()

print(a, b)