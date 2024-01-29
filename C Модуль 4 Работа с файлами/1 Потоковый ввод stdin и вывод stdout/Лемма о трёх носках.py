import sys

data = [int(line.strip()) for line in sys.stdin]

last_digit = data[-1]
player = 'Дима' if len(data) % 2 == 0 else 'Анри'

if last_digit % 2 == 0:
    print(player)
else:
    print(('Дима', 'Анри')[player == 'Дима'])
  
