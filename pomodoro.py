import datetime
import os

while 1:
    x = datetime.datetime.now()

    y = int(x.strftime("%M"))

f = open("pomodoro.txt", "a")
f.write(str(y))
f.close()

f = open('pomodoro.txt', 'r')

z = f.read()

print('start point: ' + z)

if y == int(z) + 1:
    print('its time to rest :)')
    if True:
        os.remove("pomodoro.txt")
        

