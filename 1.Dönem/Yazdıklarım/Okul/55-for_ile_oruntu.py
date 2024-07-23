
# This program displays a rectangular pattern
# of asterisks.
rows = int(input('How many rows? '))
cols = int(input('How many columns? '))

for r in range(rows):
    for c in range(cols):
        print('*', end='')
    print()

print()
print('2.sekil')


BASE_SIZE = 8

for r in range(BASE_SIZE):
    for c in range(r + 1):
        print('*', end='')
    print()

end=input()
