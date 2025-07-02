from re import IGNORECASE
import re

def normalize_jpeg(filename):
    res = re.sub(r'.jpeg$|.jpg$', r'.jpg', filename, flags=IGNORECASE)
    return res
