import numpy as np

with open("bar.txt") as f:
    text = f.read()

words = text.split()
print(len(words))
