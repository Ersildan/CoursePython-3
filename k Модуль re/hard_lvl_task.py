from bs4 import BeautifulSoup as bs
from collections import defaultdict
import sys

my_dict = defaultdict(set)
for line in sys.stdin:
    soup = bs(line, "html.parser")
    for tag in soup.find_all():
        my_dict[tag.name] |= set(tag.attrs)

for tag, values in sorted(my_dict.items()):
    print(tag + ':', ", ".join(sorted([i for i in values])))
