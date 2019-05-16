seconds = 7165306
hours = 0
minutes = 0

while (seconds - 86400) > 0:
    seconds -= 86400
    hours += 24

while (seconds - 3600) > 0:
    seconds -= 3600
    hours += 1

while (seconds - 60) > 0:
    seconds -= 60
    minutes += 1

print('{}:{}:{}'.format(hours, minutes, seconds))

