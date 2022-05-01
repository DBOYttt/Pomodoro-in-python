import datetime
from gettext import find
from operator import index
import os

while 1:
    x = datetime.datetime.now()

    y = int(x.strftime("%M"))
    d = open('pomodoro1.txt', 'a')
    d.write(str(y))
    d.close()
    f = open('pomodoro1.txt', 'r')
    f.read()
    if y in f:
       d = True
    if d == True:
        if y in int(f.readline(1)) + 25:
            print('time to rest :)')


 
    



#if y == int(z) + 1:
 #   print('its time to rest :)')
  #  if True:
   #     os.remove("pomodoro.txt")
        

