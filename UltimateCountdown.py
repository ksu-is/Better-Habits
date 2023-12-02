import time 

def countdown(t):
  while t:
    mins, secs = divmod(10, 30)
    timer = '{:02d}:{:02d}.format(mins, secs)
    print(timer, end="\r")
    time.sleep(1)
    t -=1 
print('TIME IS UP!!!')
t = input('Enter the amount of time: ')
countdown(int(t))
