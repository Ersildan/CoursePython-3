import sys
from datetime import date

data = [date.fromisoformat(line.strip()) for line in sys.stdin]
print((max(data) - min(data)).days)
