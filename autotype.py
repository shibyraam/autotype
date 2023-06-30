# path = F:\autotype\autotype.py
# pip install keyboard
import keyboard as kb
import time
x=int(input("times of typing: "))
shift = input("type your shift :")
time.sleep(3)
i=1
for i in range(x):
    if i <= x:
            kb.write(shift) 
            time.sleep(0.30)
            kb.press_and_release('enter') 
            i=i+1
    else:
        print ("finished")
                            
