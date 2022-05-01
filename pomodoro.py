import datetime
from gettext import find
import os

while 1:
    x = datetime.datetime.now()

    y = int(x.strftime("%M"))
    d = open('pomodoro1.txt', 'a')
    d.write(str(y))
    d.close()
    f = open('pomodoro1.txt', 'r')
    f.read()
    find(y in d)
    if y == y


d = open('pomodoro1', 'r')
z = d.read()
if t in z :
    print('here')


#if y == int(z) + 1:
 #   print('its time to rest :)')
  #  if True:
   #     os.remove("pomodoro.txt")
        

