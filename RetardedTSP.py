import sys

i=0
for line in sys.stdin:
    if i != 0:
        print i-1
    i += 1
