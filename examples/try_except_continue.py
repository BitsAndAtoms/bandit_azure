# bad
for i in {0,1}:
    try:
        a = i
    except:
        continue


# bad
while keep_trying:
    try:
        a = 1
    except Exception:
        continue


# bad
for i in {0,2}:
    try:
        a = i
    except ZeroDivisionError:
        continue
# good
while keep_trying:
    try:
        a = 1
    except:
        a = 2
